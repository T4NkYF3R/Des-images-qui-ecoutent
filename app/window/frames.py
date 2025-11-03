import tkinter

from app import Data
from app.window import Window, WINDOW_COLOR

FONT = ("Arial", 20, "bold")
PADX = 5
PADY = 20
COLOR = ["#FF0000", "#FF3300", "#FF6600", "#FF9900", "#FFCC00", "#FFFF00", "#CCFF00", "#99FF00", "#66FF00", "#33FF00", "#00FF00"]
ACTIVE_BG_COLOR = "black"
ACTIVE_FG_COLOR = "white"

NB_SECONDS = 1
TO_MS = 1000
AFTER_TIME = NB_SECONDS * TO_MS


class BaseFrame(tkinter.Frame):
    def __init__(self, window: Window) -> None:
        super().__init__(window, bg=WINDOW_COLOR)
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
                command=command
            )

    def create_label(self, text: str) -> tkinter.Label:
        return tkinter.Label(
            self,
            text=text,
            font=FONT,
            background=WINDOW_COLOR
        )


class StartFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window)
        self._label = None
        self._create_session_label()
        self._create_start_sutton()

        self.place(x=self._window.width, y=self._window.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = (self._window.height - self._height) / 2

    def _start_session(self) -> None:
        self._window.setSession(value=-self._window.getSession() + 1)
        self._label.configure(text="Session " + str(self._window.getSession() + 1))
        self._window.hide_frame("start")
        self._window.after(ms=AFTER_TIME, func=lambda: self._window.show_frame("image"))
        self._window.after(ms=AFTER_TIME, func=lambda: self._window.show_frame("response"))

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


class ResponseFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window=window)

        self._data = Data()

        self._value_selected: int | None = None
        self._valueSaved = 0
        self._buttons: list[tkinter.Button] = self._create_response_buttons()
        self._create_response_labels()
        self._create_save_button()

        self.place(x=self._window.width, y=self._window.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()
        self.placeX = (self._window.width - self._width) / 2
        self.placeY = self._window.height - self._height - PADY

    def _response_button_clicked(self, value: int) -> None:
        for i, button in enumerate(self._buttons):
            if i == value:
                self._value_selected = i
                button.configure(background=ACTIVE_BG_COLOR, foreground=ACTIVE_FG_COLOR)
            else:
                button.configure(background=COLOR[i], foreground="black")

    def _create_response_buttons(self) -> list:
        buttons = []
        for i in range(11):
            button = self.create_button(
                text=str(i),
                width=5,
                height=2,
                color=COLOR[i],
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
        if self._value_selected is None: return

        self._data.save_response(music=self._window.getCurrentMusic(), score=self._value_selected, stimulus="")
        self._value_selected = None
        for i, button in enumerate(self._buttons):
            button.configure(background=COLOR[i], foreground="black")
        self._valueSaved += 1

        if self._valueSaved % 4 == 0:
            self._window.setSession(value=-self._window.getSession())
            self._window.hide_frame("image")
            self._window.hide_frame("response")
            if -self._window.getSession() < 2:
                self._window.show_frame("start")
            else:
                self._window.show_frame("end")

    def _create_save_button(self) -> None:
        button: tkinter.Button = self.create_button(
            text="Enregistrer & continuer",
            width=None,
            height=None,
            color="white",
            command=self._save_button_clicked
        )
        button.grid(row=2, column=4, columnspan=3, padx=PADX, pady=PADY, sticky="ew")


class ImageFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window=window)

        self.place(x=self._window.width, y=self._window.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()


class EndFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window)
        self._create_end_label()
        self._create_end_sutton()

        self.place(x=self._window.width, y=self._window.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()
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
    "start": StartFrame,
    "response": ResponseFrame,
    "image": ImageFrame,
    "end": EndFrame
}