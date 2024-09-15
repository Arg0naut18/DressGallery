from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Dict
from src.logging import logger
from datetime import datetime
import pytz
import json


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
            if 'Timestamp' in elem:
                elem['Timestamp'] = json.dumps(elem['Timestamp'], default=str)
        return elems

    @staticmethod
    async def update(collection: AsyncIOMotorCollection, identifier: Dict, data: Dict):
        logger.info("Updating Data")
        data['Timestamp'] = datetime.now(tz=pytz.timezone('Asia/Calcutta'))
        await collection.replace_one(filter=identifier, replacement=data)

    @staticmethod
    async def delete(collection: AsyncIOMotorCollection, identifier: Dict):
        logger.info("Deleting Data")
        await collection.delete_one(filter=identifier)
