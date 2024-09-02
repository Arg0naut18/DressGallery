from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Dict
from src.logging import logger


class MongoUtil:
    @staticmethod
    async def insert(collection: AsyncIOMotorCollection, data: Dict):
        logger.info(data)
        await collection.insert_one(data)

    @staticmethod
    async def find(collection: AsyncIOMotorCollection, data: Dict = None, length=1000) -> List:
        cursor = collection.find(data)
        elems = await cursor.to_list(length=length)
        for elem in elems:
            if '_id' in elem:
                elem['_id'] = str(elem['_id'])
        return elems

    @staticmethod
    async def update(collection: AsyncIOMotorCollection, identifier: Dict, data: Dict):
        await collection.update_one(filter=identifier, update=data)

    @staticmethod
    async def delete(collection: AsyncIOMotorCollection, identifier: Dict):
        await collection.delete_one(filter=identifier)
