import os


class MongoConfigs:
    username = os.getenv("MONGO_USERNAME")
    password = os.getenv("MONGO_PASSWORD")
    app_name = os.getenv("MONGO_APPNAME")
    mongo_srv = f"mongodb+srv://{username}:{password}@gallery.bekey7e.mongodb.net/?retryWrites=true&w=majority&appName={app_name}"
