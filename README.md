# Clash Royale Deck Brain

AI-powered deck analysis, recommendations, and friend group matchups.

## Quick Start

```bash
# Start the full stack
docker-compose up --build

# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## Features
- Deck strength prediction vs meta
- Player profile analysis
- Personalized deck recommendations
- Friend group matchup comparisons

## Project Structure
- `backend/` - FastAPI + PostgreSQL + ML
- `frontend/` - Next.js + React + Tailwind
- `docker-compose.yml` - Full stack orchestration

## Next Steps
1. Download Kaggle datasets
2. Train LightGBM model
3. Populate database with meta decks
4. Integrate RoyaleAPI
5. Deploy to cloud

