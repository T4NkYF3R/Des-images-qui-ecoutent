import tkinter
from pathlib import Path
from PIL import Image as Img
from PIL import ImageOps as ImgOps
from PIL import ImageTk as ImgTk

from app import Data, BACKGROUND_COLOR, RESPONSE_BUTTON_COLOR, ACTIVE_BG_BUT_COLOR, ACTIVE_FG_BUT_COLOR, FONT, PADX, PADY, MAX_WIDTH_IMAGE, MAX_HEIGHT_IMAGE, NB_SESSION, NB_IMAGE_SESSION, AFTER_TIME
from app.window import Window
from app.assets import Image


class BaseFrame(tkinter.Frame):
    def __init__(self, window: Window) -> None:
        super().__init__(window, bg=BACKGROUND_COLOR)
        self._window = window
        self._width = 0
        self._height = 0
        self.placeX: float = 0
        self.placeY: float = 0

    def create_button(self, text: str, color: str, command, width: int | None, height: int | None) -> tkinter.Button:
        return tkinter.Button(
                self,
                text=text,
                font=FONT,
                width=width,
                height=height,
                background=color,
                foreground="black",
                activebackground="black",
                activeforeground="white",
                bd=0,
                highlightthickness=2,
                highlightbackground="black",
                command=command
            )

    def create_label(self, text: str) -> tkinter.Label:
        return tkinter.Label(
            self,
            text=text,
            font=FONT,
            background=BACKGROUND_COLOR
        )

    def _getSize(self) -> None:
        self.place(x=self._window.width, y=self._window.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()
        self.update()

    def getSize(self) -> tuple[int, int]:
        return (self._width, self._height)


class GroupFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window)
        self._buttons: list[tkinter.Button] = []
        self._buttonSelected = False
        self._create_group_button()
        self._create_group_label()
        self._getSize()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = (self._window.height - self._height) / 2

    def _setGroupe(self, groupe: bool) -> None:
        self._buttonSelected = True
        for i, button in enumerate(self._buttons):
            if i == int(groupe):
                button.configure(background=ACTIVE_BG_BUT_COLOR, foreground=ACTIVE_FG_BUT_COLOR)
            else:
                button.configure(background="white", foreground="black")
        self._window.setControle(status=groupe)

    def _validate(self) -> None:
        if self._buttonSelected is not True:
            return
        self._window.hide_frame("group")
        self._window.show_frame("start")

    def _create_group_button(self) -> None:
        groupes = ["Expérimental", "Contrôle"]
        for i in range(2):
            button = self.create_button(
                text=groupes[i],
                color="white",
                width=20,
                height=None,
                command=lambda groupe=i:self._setGroupe(groupe=groupe)
            )
            button.grid(row=i + 1, column=0, pady=2)
            self._buttons.append(button)

        button = self.create_button(
            text="Valider",
            color="white",
            width=None,
            height=None,
            command=self._validate
        )
        button.grid(row=3, column=0, pady=PADY)

    def _create_group_label(self) -> None:
        label = self.create_label(text="Sélectionnez le groupe à évaluer")
        label.grid(row=0, column=0)

class StartFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window)
        self._label = None
        self._create_session_label()
        self._create_start_sutton()
        self._getSize()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = (self._window.height - self._height) / 2

    def _start_session(self) -> None:
        self._window.setSession(value=-self._window.getSession() + 1)
        self._label.configure(text="Session " + str(self._window.getSession() + 1))
        self._window.hide_frame("start")
        imageFrame: ImageFrame = self._window.getFrame("image")
        imageFrame.setNextImage()
        time = AFTER_TIME if self._window.getControle() is False else 0
        self._window.after(ms=time, func=lambda: self._window.show_frame("image"))
        self._window.after(ms=time, func=lambda: self._window.show_frame("response"))

    def _create_start_sutton(self) -> None:
        button = self.create_button(
            text="Commencer",
            color="white",
            width=None,
            height=None,
            command=self._start_session
        )
        button.grid(row=1, column=0)
        return button

    def _create_session_label(self) -> None:
        self._label = self.create_label(text="Session " + str(self._window.getSession() + 1))
        self._label.grid(row=0, column=0)


class ImageFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window=window)
        self._image = Image()
        self._imagesLists = self._image.makeGroupeSession()
        self._label: BaseFrame = self.create_label(text="Image undefined")
        self._label.grid(row=0, column=0)
        self._currentImage = None
        self._photo = None
        self._idx = 0

    def getCurrentImage(self) -> str | None:
        return self._currentImage

    def setNextImage(self) -> None:
        self._currentImage = self._imagesLists[self._idx]
        self._idx += 1
        image = Img.open(self._currentImage)
        image = ImgOps.exif_transpose(image=image)
        width , height = image.size
        ratio = min(MAX_WIDTH_IMAGE * self._window.width / width, MAX_HEIGHT_IMAGE * self._window.height / height)
        width = int(width * ratio)
        height = int(height * ratio)
        image = image.resize(size=(width, height))
        self._photo = ImgTk.PhotoImage(image=image)
        self._label.configure(image=self._photo)

        self._getSize()
        responseFrame: BaseFrame = self._window.getFrame("response")
        _, rHeight = responseFrame.getSize()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = (self._window.height - rHeight - self._height) / 2


class ResponseFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window=window)

        self._data = Data()

        self._value_selected: int | None = None
        self._valueSaved = 0
        self._buttons: list[tkinter.Button] = self._create_response_buttons()
        self._create_response_labels()
        self._create_save_button()
        self._getSize()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = self._window.height - self._height - PADY

    def _response_button_clicked(self, value: int) -> None:
        for i, button in enumerate(self._buttons):
            if i == value:
                self._value_selected = i
                button.configure(background=ACTIVE_BG_BUT_COLOR, foreground=ACTIVE_FG_BUT_COLOR)
            else:
                button.configure(background=RESPONSE_BUTTON_COLOR[i], foreground="black")

    def _create_response_buttons(self) -> list:
        buttons = []
        for i in range(11):
            button = self.create_button(
                text=str(i),
                width=5,
                height=2,
                color=RESPONSE_BUTTON_COLOR[i],
                command=lambda value=i: self._response_button_clicked(value=value)
            )
            button.grid(row=1, column=i, padx=PADX)
            buttons.append(button)
        return buttons

    def _create_response_labels(self) -> None:
        label_list: list[str] = ["Négatif", "Neutre", "Positif"]
        for i in range(3):
            label = self.create_label(label_list[i])
            label.grid(row=0, column=i*5)

    def _save_button_clicked(self) -> None:
        if self._value_selected is None:
            return

        musicName = Path(self._window.getCurrentMusic()).stem if self._window.getControle() is False else "No music"
        imageFrame: ImageFrame = self._window.getFrame("image")
        current_image = imageFrame.getCurrentImage()
        imageName = Path(current_image if current_image is not None else "Undefined").stem
        self._data.save_response(music=musicName, score=self._value_selected, stimulus=imageName)
        self._value_selected = None
        for i, button in enumerate(self._buttons):
            button.configure(background=RESPONSE_BUTTON_COLOR[i], foreground="black")
        self._valueSaved += 1

        if self._valueSaved % NB_IMAGE_SESSION == 0:
            self._window.setSession(value=-self._window.getSession())
            self._window.hide_frame("image")
            self._window.hide_frame("response")
            if -self._window.getSession() < NB_SESSION:
                self._window.show_frame("start")
            else:
                self._window.show_frame("end")
        else:
            imageFrame: ImageFrame = self._window.getFrame("image")
            imageFrame.setNextImage()
            self._window.show_frame("image")

    def _create_save_button(self) -> None:
        button: tkinter.Button = self.create_button(
            text="Enregistrer & continuer",
            width=None,
            height=None,
            color="white",
            command=self._save_button_clicked
        )
        button.grid(row=2, column=4, columnspan=3, padx=PADX, pady=PADY, sticky="ew")


class EndFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window)
        self._create_end_label()
        self._create_end_sutton()
        self._getSize()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = (self._window.height - self._height) / 2

    def _end_session(self) -> None:
        self._window.stop()

    def _create_end_sutton(self) -> None:
        button = self.create_button(
            text="Quitter",
            color="white",
            width=None,
            height=None,
            command=self._end_session
        )
        button.grid(row=1, column=0)
        return button

    def _create_end_label(self) -> None:
        self._label = self.create_label(text="Fin de l'expérience")
        self._label.grid(row=0, column=0)


FRAME_LIST = {
    "group": GroupFrame,
    "start": StartFrame,
    "image": ImageFrame,
    "response": ResponseFrame,
    "end": EndFrame
}