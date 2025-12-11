import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://crdb:crdb_pass@postgres:5432/crdb")
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
ROYALE_API_KEY = os.getenv("ROYALE_API_KEY", "")
