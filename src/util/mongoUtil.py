from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List


class MongoUtil:
    @staticmethod
    async def insert(collection: AsyncIOMotorCollection, data):
        await collection.insert_one(data.__dict__)

    @staticmethod
    async def find(collection: AsyncIOMotorCollection, data: dict = None, length=1000) -> List:
        cursor = collection.find(data)
        elems = await cursor.to_list(length=length)
        for elem in elems:
            elem['_id'] = str(elem['_id'])
        return elems

    @staticmethod
    async def update(collection: AsyncIOMotorCollection, identifier: dict, data: dict):
        await collection.update_one(filter=identifier, update=data)
