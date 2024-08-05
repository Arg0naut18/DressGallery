from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List


class MongoUtil:
    @staticmethod
    async def insert(collection: AsyncIOMotorCollection, data):
        await collection.insert_one(data)

    @staticmethod
    async def find(collection: AsyncIOMotorCollection, data: dict = None, length=1000) -> List:
        cursor = collection.find(data)
        return await cursor.to_list(length=length)

    @staticmethod
    async def update(collection: AsyncIOMotorCollection, identifier: dict, data: dict):
        await collection.update_one(filter=identifier, update=data)
