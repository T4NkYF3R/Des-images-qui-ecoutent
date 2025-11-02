import tkinter

from app import Data
from app.window import Window, WINDOW_COLOR

FONT = ("Arial", 20, "bold")
PADX = 5
PADY = 20
COLOR = ["#FF0000", "#FF3300", "#FF6600", "#FF9900", "#FFCC00", "#FFFF00", "#CCFF00", "#99FF00", "#66FF00", "#33FF00", "#00FF00"]
ACTIVE_BG_COLOR = "black"
ACTIVE_FG_COLOR = "white"


class BaseFrame(tkinter.Frame):
    def __init__(self, window: Window) -> None:
        super().__init__(window, bg=WINDOW_COLOR)
        self._parent = window
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


class ResponseFrame(BaseFrame):
    def __init__(self, window: Window) -> None:
        super().__init__(window=window)

        self._data = Data()

        self._value_selected: int | None = None
        self._buttons: list[tkinter.Button] = self._create_response_buttons()
        self._create_response_labels()
        self._create_save_button()

        self.place(x=self._parent.width, y=self._parent.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()
        self.placeX = (self._parent.width - self._width) / 2
        self.placeY = self._parent.height - self._height - PADY

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
        if self._value_selected is not None:
            self._data.save_response(self._value_selected)
            for i, button in enumerate(self._buttons):
                button.configure(background=COLOR[i], foreground="black")

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

        self.place(x=self._parent.width, y=self._parent.height)
        self.update()
        self._width = self.winfo_width()
        self._height = self.winfo_height()
        self.place_forget()


FRAME_LIST = {
    "response": ResponseFrame,
    "image": ImageFrame
}