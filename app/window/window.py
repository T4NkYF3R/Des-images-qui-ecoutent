import tkinter
from threading import Thread

from app import BACKGROUND_COLOR


class Window(tkinter.Tk):
    def __init__(self, titleWindow: str) -> None:
        super().__init__()
        self.title(string=titleWindow)
        self.attributes("-fullscreen", True)
        self.configure(background=BACKGROUND_COLOR)
        self.bind("<Escape>", func=self._close_window)
        self.width = 1920
        self.height = 1080

        self._frames = {}
        self._session = 0

        from app.assets import Music
        self._musicPlayer = Music(self)
        self._musicThread = Thread(target=self._musicPlayer.run, daemon=True)

    def _close_window(self, event=None) -> None:
        self.destroy()

    def _start_music_thread(self) -> None:
        self._musicThread.start()

    def getFrame(self, name: str):
        return self._frames[name]

    def add_frame(self, name: str, frameClass) -> None:
        self._frames[name] = frameClass(self)

    def show_frame(self, name: str) -> None:
        from app.window import BaseFrame
        frame: BaseFrame = self._frames[name]
        frame.place(x=frame.placeX, y=frame.placeY)

    def hide_frame(self, name: str) -> None:
        from app.window import BaseFrame
        frame: BaseFrame = self._frames[name]
        frame.place_forget()
        self.update()

    def setSession(self, value: int) -> None:
        self._session = value

    def getSession(self) -> int:
        return self._session

    def getCurrentMusic(self) -> str:
        return self._musicPlayer.getMusicLoaded()

    def stop(self) -> None:
        self._musicPlayer.stop()
        self._close_window()

    def run(self) -> None:
        self._start_music_thread()
        self.show_frame("group")
        self.mainloop()
