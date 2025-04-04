# DigiRoboticApp-Vision

Vision Processing Service built with Python.

## Tech Stack
- Python 3.9+
- FastAPI
- Docker

## Development Setup

### Prerequisites
- Docker Desktop
- Python 3.9+
- Git

### Setup Instructions
```bash
# Clone the repository
git clone git@github.com:sonnyvedder/DigiRoboticApp-Vision.git
cd DigiRoboticApp-Vision

# Create environment file
copy .env.example .env

# Setup Python virtual environment (for local development)
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# Start the service
docker-compose up -d