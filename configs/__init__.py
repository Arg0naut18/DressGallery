import os


class MongoConfigs:
    db_name = os.getenv("MONGO_DB", "mongo_db")
    mongo_srv = os.getenv("MONGO_SRV", "mongo_srv")
    mongo_collection = os.getenv("MONGO_COLLECTION", "mongo_collection")
