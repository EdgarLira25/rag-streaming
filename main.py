import uvicorn
from src.app import app
from src.apps.shared.database.connector import Database


if __name__ == "__main__":
    Database().migrate_all()
    uvicorn.run(app, host="0.0.0.0", port=8000)
