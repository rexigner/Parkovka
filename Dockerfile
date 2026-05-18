FROM python:3.13-slim

WORKDIR /app

# Install deps first (better caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . /app

# Default command: run the bot
CMD ["python", "main.py"]

