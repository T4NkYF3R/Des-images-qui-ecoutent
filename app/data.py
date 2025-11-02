import csv

from app import DATA

CSV_FILE = "reponses.csv"
CSV_PATH = DATA / CSV_FILE

class Data:
    def __init__(self) -> None:
        self._create_data_folder()
        self._initCSV()

    def _create_data_folder(self) -> None:
        DATA.mkdir(parents=True, exist_ok=True)

    def _initCSV(self) -> None:
        if CSV_PATH.exists() is not True:
            with open(CSV_PATH, "x", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(["Musique", "Note [0-10]", "Stimuli neutre"])

    def save_response(self, music: str, score: str, stimulus: str) -> None:
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow([music, score, stimulus])