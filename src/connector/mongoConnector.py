from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from src.logging import logger
from configs import MongoConfigs
from retrying import retry


class MongoConnector:
    @retry()
    def __init__(self) -> None:
        try:
            self.cluster = AsyncIOMotorClient(MongoConfigs.mongo_srv)
            self.database = self.cluster[MongoConfigs.db_name]
        except Exception as e:
            logger.error(e)

    def get_collection(self, name: str) -> AsyncIOMotorCollection:
        return self.database[name]


db = MongoConnector()
