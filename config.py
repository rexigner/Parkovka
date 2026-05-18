# ─────────────────────────────────────────────
#  config.py  —  All tuneable settings in one place
# ─────────────────────────────────────────────

BOT_TOKEN = "8656938382:AAEvne0reDuo160k7gibE76Dxr8xm5HV-pM"   # paste from @BotFather
DB_PATH   = "parking.db"

# ── City bounding boxes (south, west, north, east) ──────────────────────────
CITIES = {
    "minsk":  (53.80, 27.40, 53.95, 27.70),
    "moscow": (55.55, 37.32, 55.92, 37.85),
}

# ── Search parameters ────────────────────────────────────────────────────────
MAX_RESULTS        = 5     # spots returned per query
SEARCH_RADIUS_KM   = 1.5   # how far to look

# ── Crowdsource / decay ──────────────────────────────────────────────────────
REPORT_DECAY_MINUTES = 20  # reports older than this are ignored
CONFIRM_THRESHOLD    = 3   # "full" reports needed to hide a spot
