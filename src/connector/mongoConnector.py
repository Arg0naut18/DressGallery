from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from src.logging.logger import logger
from src.constants import MongoConstants
from configs import MongoConfigs
from retrying import retry


class MongoConnector:
    @retry()
    def __init__(self) -> None:
        try:
            self.cluster = AsyncIOMotorClient(MongoConfigs.mongo_srv)
            self.database = self.cluster[MongoConstants.DB_NAME]
        except Exception as e:
            logger.error(e)

    def get_collection(self, name: str) -> AsyncIOMotorCollection:
        return self.database[name]

    @classmethod
    def get_connector(cls):
        cls.__init__()
        return cls
