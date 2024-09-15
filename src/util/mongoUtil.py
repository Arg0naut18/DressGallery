from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Dict
from src.logging import logger
from datetime import datetime
import pytz


class MongoUtil:
    @staticmethod
    async def insert(collection: AsyncIOMotorCollection, data: Dict):
        logger.info("Inserting Data")
        data['Timestamp'] = datetime.now(tz=pytz.timezone('Asia/Calcutta'))
        await collection.insert_one(data)

    @staticmethod
    async def find(collection: AsyncIOMotorCollection, data: Dict = None, length=1000) -> List:
        logger.info("Finding Data")
        cursor = collection.find(data)
        elems = await cursor.to_list(length=length)
        for elem in elems:
            if '_id' in elem:
                elem['_id'] = str(elem['_id'])
        return elems

    @staticmethod
    async def update(collection: AsyncIOMotorCollection, identifier: Dict, data: Dict):
        logger.info("Updating Data")
        data['Timestamp'] = datetime.now(tz=pytz.timezone('Asia/Calcutta'))
        await collection.update_one(filter=identifier, update=data)

    @staticmethod
    async def delete(collection: AsyncIOMotorCollection, identifier: Dict):
        logger.info("Deleting Data")
        await collection.delete_one(filter=identifier)
