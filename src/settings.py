import os

DATABASE_URI = os.environ.get("DATABASE_URI", "")

# Use openssl rand -hex 32 to gen SECRET_KEY
SECRET_KEY = os.environ.get("SECRET_KEY", "")

ALGORITHM = os.environ.get("ALGORITHM", "")
TOKEN_TIME = int(os.environ.get("TOKEN_TIME", 15 * 60))

OPEN_SUBTITLE_API_KEY = os.environ.get("OPEN_SUBTITLE_API_KEY", "")
OPEN_SUBTITLE_USERNAME = os.environ.get("OPEN_SUBTITLE_USERNAME", "")
OPEN_SUBTITLE_PASSWORD = os.environ.get("OPEN_SUBTITLE_PASSWORD", "")
STORAGE_LOCATION = os.environ.get("STORAGE_LOCATION", "storage/")

REFRESH_TOKEN_TIME = int(os.environ.get("REFRESH_TOKEN_TIME", 120 * 60))
