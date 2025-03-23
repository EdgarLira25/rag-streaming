import os

DATABASE_URI = os.environ.get("DATABASE_URI", "")

# Use openssl rand -hex 32 to gen SECRET_KEY
SECRET_KEY = os.environ.get("SECRET_KEY", "")

ALGORITHM = os.environ.get("ALGORITHM", "")
TOKEN_TIME = int(os.environ.get("TOKEN_TIME", 15 * 60))
REFRESH_TOKEN_TIME = int(os.environ.get("REFRESH_TOKEN_TIME", 120 * 60))
