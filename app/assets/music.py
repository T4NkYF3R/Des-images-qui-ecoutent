import pygame
import random
from time import sleep

from app import MUSIC, NB_SESSION, SLEEP_TIME, NB_SECONDS
from app.window import Window

class Music:
    def __init__(self, window: Window) -> None:
        self._window = window
        pygame.mixer.init()
        self._running = True
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
                    print(f"[assets/music] Unsupported extension for music file '{music.name}'")
        if len(musics) < NB_SESSION:
            raise RuntimeError(f"[assets/music] Not enought music to play ({len(music)}/{NB_SESSION} required).")
        random.shuffle(musics)
        return musics

    def _load(self, session: int) -> None:
        self._currentTrack = self._musics[session - 1]
        pygame.mixer.music.load(filename=self._currentTrack)

    def _play(self) -> None:
        pygame.mixer.music.play(loops=-1)

    def _stop(self) -> None:
        pygame.mixer.music.stop()

    def stop(self) -> None:
        self._running = False
        pygame.mixer.music.stop()
        pygame.mixer.quit()

    def getMusicLoaded(self) -> str | None:
        return self._currentTrack

    def _check_session_change(self) -> None:
        while self._running:
            session = self._window.getSession()
            if session < 0:
                self._stop()
                if session < -NB_SESSION:
                    return
            elif self._session != session:
                self._session = session
                break
            sleep(SLEEP_TIME)

    def run(self) -> None:
        self._session = self._window.getSession()
        self._check_session_change()
        if self._window.getControle() is True:
            self.stop()
            return
        self._load(session=self._session)
        self._play()
        sleep(NB_SECONDS)
        self._check_session_change()
        self._stop()
        self._load(session=self._session)
        self._play()
        self._check_session_change()
