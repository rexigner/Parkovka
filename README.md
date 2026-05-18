# 🅿️ Free Parking Bot — Minsk & Moscow

A Telegram bot that finds the nearest **free parking spots** using
OpenStreetMap data + live crowd-sourced occupancy reports.

---

## File structure

```
parking_bot/
├── config.py         ← All settings (token, cities, radii, decay)
├── database.py       ← SQLite schema + connection helper
├── osm_fetcher.py    ← Pulls free-parking data from Overpass API
├── engine.py         ← Haversine search + decayed occupancy scoring
├── main.py           ← Telegram bot (aiogram v3)
└── requirements.txt
```

---

## Quick start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Create a bot
1. Open Telegram → search for **@BotFather**
2. Send `/newbot` and follow the prompts
3. Copy the token it gives you

### 3. Paste your token
Open `config.py` and replace:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

### 4. Seed the database (one-time, ~1–2 minutes)
```bash
# Both cities
python osm_fetcher.py

# Or just one city
python osm_fetcher.py minsk
python osm_fetcher.py moscow
```
This queries Overpass API and writes all free parking spots into `parking.db`.

### 5. Run the bot
```bash
python main.py
```

---

## Bot commands

| Command  | Description                          |
|----------|--------------------------------------|
| `/start` | Welcome message + location button   |
| `/find`  | Ask for location again               |
| `/help`  | Explains colours, courtyard warning  |
| `/stats` | Shows how many spots are in the DB  |

Then simply **share your location** and the bot returns the nearest
free spots with live map pins and report buttons.

---

## How the occupancy model works

Every time a user taps ✅ *Still free* or 🔴 *Full/taken*, a row is
written to the `reports` table with a UTC timestamp.

When calculating a spot's status, only reports from the **last 20 minutes**
are considered (configurable via `REPORT_DECAY_MINUTES`).

| Condition                        | Status shown |
|----------------------------------|--------------|
| < 3 "full" reports, or none      | 🟢 Free      |
| More "full" than "free" reports  | 🟡 Likely full |
| ≥ 3 "full" reports               | 🔴 Full (hidden from results) |

This mirrors a signal-decay approach — old reports carry zero weight so
stale data doesn't mislead drivers.

---

## Adding more cities

In `config.py`, add a bounding box (south, west, north, east):

```python
CITIES = {
    "minsk":  (53.80, 27.40, 53.95, 27.70),
    "moscow": (55.55, 37.32, 55.92, 37.85),
    "spb":    (59.85, 30.10, 60.05, 30.55),   # Saint Petersburg example
}
```

Then run `python osm_fetcher.py spb` to seed the new city.

---

## Keeping data fresh

Set up a weekly cron job to re-fetch OSM data (new spots get added
by the OSM community over time):

```bash
# crontab -e
0 3 * * 1   cd /path/to/parking_bot && python osm_fetcher.py >> osm.log 2>&1
```

---

## Notes on courtyard spots

Many "free" spots in Russian and Belarusian cities are inside residential
courtyards. These are tagged with `certainty = low` in the database and
show a ⚠️ warning in the bot. Drivers should always check for barriers
(шлагбаум) before entering.
