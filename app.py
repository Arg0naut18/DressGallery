from fastapi import FastAPI
from src.model.cloth import Cloth
from src.connector.mongoConnector import MongoConnector
from src.util.mongoUtil import MongoUtil
from src.logging.logger import logger
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()
db = MongoConnector()
mongo_collection = db.get_collection("Clothes")


@app.post("/add_dress/")
async def add_dress(cloth: Cloth):
    try:
        await MongoUtil.insert(mongo_collection, cloth)
        return {"StatusCode": 200, "Message": "Ok"}
    except Exception as e:
        logger.error(e)
        return {"StatusCode": 400, "Message": "Error Occurred"}


@app.get("/view_dress/")
async def view_dress(name: str = None, color: str = None, tags: list = None, max_age: int = None):
    filter_dict = {}
    if name:
        filter_dict['name'] = name
    if color:
        filter_dict['color'] = color
    if tags:
        filter_dict['tags'] = {"$all": tags}
    if max_age:
        filter_dict['age'] = {"$lte": max_age}
    dresses = await MongoUtil.find(mongo_collection, filter_dict)
    return {"StatusCode": 200, "Message": str(dresses)}


@app.put("/update_dress/{dress_id}")
async def update_dress(dress_id: int, updates: dict):
    await MongoUtil.update(mongo_collection, {'id': dress_id}, updates)
