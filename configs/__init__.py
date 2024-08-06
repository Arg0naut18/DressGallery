import os


class MongoConfigs:
    db_name = os.getenv("MONGO_DB")
    mongo_srv = os.getenv("MONGO_SRV")
