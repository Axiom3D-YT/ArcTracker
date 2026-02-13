# ARC Raiders Event Tracker

A live event tracker for ARC Raiders that displays active and upcoming events with real-time countdowns.

## Features

- Real-time event tracking from MetaForge API
- Dynamic filtering by map and event type
- Live countdown timers
- Responsive, premium dark UI
- Event descriptions and icons

## Quick Start (Local Development)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Access at: http://localhost:5000

## Docker Deployment

See [UNRAID_DEPLOY.md](UNRAID_DEPLOY.md) for detailed Unraid deployment instructions.

### Quick Docker Start

```bash
# Build and run with docker-compose
docker-compose up -d

# Or build and run manually
docker build -t arctracker .
docker run -d -p 5000:5000 --name arctracker arctracker
```

## API Credit

Data provided by [MetaForge](https://metaforge.app/arc-raiders)

## Project Structure

```
ArcTracker/
├── app.py              # Flask application
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
└── UNRAID_DEPLOY.md   # Unraid deployment guide
```
