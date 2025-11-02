import tkinter
from threading import Thread

WINDOW_COLOR = "#F4EDDE"
BUTTON_SIZE = 5
COLOR = ["#FF0000", "#FF3300", "#FF6600", "#FF9900", "#FFCC00", "#FFFF00", "#CCFF00", "#99FF00", "#66FF00", "#33FF00", "#00FF00"]
ACTIVE_BG_COLOR = "black"
ACTIVE_FG_COLOR = "white"

NB_MS = 100
SECOND_IN_MS = 60000
SLEEP_TIME = NB_MS * 1 / SECOND_IN_MS

class Window(tkinter.Tk):
    def __init__(self, titleWindow: str) -> None:
        super().__init__()
        self.title(string=titleWindow)
        self.attributes("-fullscreen", True)
        self.configure(background=WINDOW_COLOR)
        self.bind("<Escape>", func=self._close_window)
        self.width = 1920
        self.height = 1080

        self._frames = {}
        self._session = 1

        from app.assets import Music
        self._musicPlayer = Music(self)
        self._musicThread = Thread(target=self._musicPlayer.run, daemon=True)

    def _close_window(self, event=None) -> None:
        self.destroy()

    def add_frame(self, name: str, frameClass):
        self._frames[name] = frameClass(self)

    def show_frame(self, name: str) -> None:
        from app.window import BaseFrame
        frame: BaseFrame = self._frames[name]
        frame.place(x=frame.placeX, y=frame.placeY)

    def hide_frame(self, name: str) -> None:
        from app.window import BaseFrame
        frame: BaseFrame = self._frames[name]
        frame.place_forget()

    def getSession(self) -> int:
        return self._session

    def run(self) -> None:
        self._musicThread.start()
        self.after(ms=2 * 1000, func=lambda: self.show_frame("image"))
        self.after(ms=2 * 1000, func=lambda: self.show_frame("response"))
        self.mainloop()
