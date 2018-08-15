import os
from diary.main import create_app
from config import app_config

config = os.getenv("APP_SETTINGS")
# include configurations
app = create_app(config)

if __name__ == '__main__':
    app.run()
