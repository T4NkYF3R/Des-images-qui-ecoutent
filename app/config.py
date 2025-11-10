from pathlib import Path


# ========== CONFIG ==========
NB_SESSION = 2
NB_IMAGE_SESSION = 5
CSV_FILE = "reponses.csv"


# ========== FILES ==========
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ASSETS = ROOT / "assets"
IMAGE = ASSETS / "image"
MUSIC = ASSETS / "music"
CSV_PATH = DATA / CSV_FILE


# ========== COLORS ==========
BACKGROUND_COLOR = "#F4EDDE"
RESPONSE_BUTTON_COLOR = ["#CECECE", "#D2C6C2", "#D7CBC4", "#DDD1C6", "#E3D6C8", "#E8DCCA", "#E3D6C8", "#DDD1C6", "#D7CBC4", "#D2C6C2", "#CECECE"]
ACTIVE_BG_BUT_COLOR = "black"
ACTIVE_FG_BUT_COLOR = "white"


# ========== FONT ==========
FONT = ("Arial", 20, "bold")


# ========== SIZES ==========
PADX = 5
PADY = 20

MAX_WIDTH_IMAGE = 500
MAX_HEIGHT_IMAGE = 500


# ========== TIMES ==========
NB_SECONDS = 1
NB_MS = 100
SECOND_TO_MS = 1000
AFTER_TIME = NB_SECONDS * SECOND_TO_MS
SLEEP_TIME = NB_MS * 1 / SECOND_TO_MS