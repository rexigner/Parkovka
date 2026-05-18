# 🅿️ Free Parking Bot - Setup Instructions

## Bot Status
✅ **REAL PROGRAM - READY TO WORK**

## Project Overview
This is a fully functional Telegram bot that finds free parking spots in Minsk (Belarus) and Moscow (Russia) using OpenStreetMap data and live crowd-sourced reports.

## Database Status
- **Total Parking Spots**: 27,640
- **Minsk**: 9,034 parking spots
- **Moscow**: 18,606 parking spots

## How to Start the Bot

### Option 1: Using the startup script (recommended)
```bash
cd /home/rexigner/parking_bot
./start_bot.sh
```

### Option 2: Manual start
```bash
cd /home/rexigner/parking_bot
source venv/bin/activate
python main.py
```

## Bot Commands
- `/start` - Welcome message + location button
- `/find` - Ask for location again
- `/help` - Explains colors, courtyard warning
- `/stats` - Shows database statistics

## How to Use
1. Start the bot
2. Open Telegram and find your bot
3. Click "📍 Share my location" when prompted
4. The bot will show you the nearest free parking spots
5. After visiting a spot, tap "✅ Still free" or "🔴 Full/taken" to help other drivers

## Features
- 🟢 Shows free parking spots
- 🟡 Shows spots with mixed reports (approach with caution)
- 🔴 Hides confirmed full spots
- Uses 20-minute decay for reports (no stale data)
- Shows courtyard spots with ⚠️ warnings

## Technical Details
- **Framework**: aiogram v3
- **Database**: SQLite
- **Data Source**: OpenStreetMap via Overpass API
- **Cities**: Minsk, Moscow (ready for more)
- **Search Radius**: 1.5 km
- **Max Results**: 5 spots per query

The bot is ready to use immediately!