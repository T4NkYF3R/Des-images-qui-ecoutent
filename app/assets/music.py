import pygame
import random
from time import sleep

from app import MUSIC
from app.window import Window

NB_MS = 100
SECOND_IN_MS = 60000
SLEEP_TIME = NB_MS * 1 / SECOND_IN_MS

class Music:
    def __init__(self, window: Window) -> None:
        self._window = window
        pygame.mixer.init()
        self._currentTrack = None
        self._musics = self._loadMusics()
        self._session = 0

    def _loadMusics(self) -> list[str]:
        extensions = (".mp3", ".wav", ".ogg", ".flac")
        musics = []
        for music in MUSIC.iterdir():
            if music.is_file():
                if music.suffix.lower() in extensions:
                    musics.append(music)
                else:
                    print(f"Unsupported extension for file '{music.name}'")
        if len(musics) < 2:
            raise RuntimeError("Not enought music to play.")
        if random.random() >= 0.5:
            musics.reverse()
            return musics
        else:
            return musics

    def _load(self, session: int = 1 | 2) -> None:
        match session:
            case 1: self._currentTrack = self._musics[0]
            case 2: self._currentTrack = self._musics[1]
        pygame.mixer.music.load(filename=self._currentTrack)

    def _play(self) -> None:
        pygame.mixer.music.play(loops=-1)

    def _stop(self) -> None:
        pygame.mixer.music.stop()

    def run(self) -> None:
        self._session = self._window.getSession()
        self._load(session=self._session)
        self._play()
        sleep(30)
        while True:
            session = self._window.getSession()
            if self._session != session:
                self._session = session
                break
            sleep(SLEEP_TIME)
        self._stop()
        self._load(session=self._session)
        self._play()
