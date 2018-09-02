import os
from diary.main import create_app

config = os.getenv("APP_SETTINGS")
# include configurations
app = create_app(config)

if __name__ == '__main__':
    app.run(use_reloader=False)
