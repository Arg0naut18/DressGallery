from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.model.cloth import Cloth
from src.connector.mongoConnector import MongoConnector
from src.util.mongoUtil import MongoUtil
from src.logging.logger import logger
from dotenv import load_dotenv
from bson import ObjectId


load_dotenv()
app = FastAPI()
db = MongoConnector()
mongo_collection = db.get_collection()
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/add_dress/")
async def add_dress(cloth: Cloth):
    try:
        await MongoUtil.insert(mongo_collection, cloth)
        return JSONResponse(status_code=200, content="Success!")
    except Exception as e:
        logger.error(e)
        return JSONResponse(status_code=400, content=f"Error Occurred:\n{e}")


@app.get("/view_dress/")
async def view_dress(name: str = None, color: str = None, tags: str = None, year_of_purchase: int = None, brand: str = None):
    filter_dict = {}
    if name and name.strip():
        filter_dict['name'] = name.strip()
    if color and color.strip():
        filter_dict['color'] = color.strip()
    if tags and tags.strip():
        filter_dict['tags'] = {"$in": tags.split(',')}
    if brand and brand.strip():
        filter_dict['brand'] = brand
    if year_of_purchase and year_of_purchase.strip():
        filter_dict.update(
            {"$or": [{"age": {"$gte": year_of_purchase}}, {"age": None}]})
    dresses = await MongoUtil.find(mongo_collection, filter_dict)
    return JSONResponse(content=dresses, status_code=200)


@app.put("/update_dress/{dress_id}")
async def update_dress(dress_id: str, cloth: Cloth):
    print(dress_id)
    print(cloth)
    await MongoUtil.update(mongo_collection, {'_id': ObjectId(dress_id)}, cloth.__dict__)
    return JSONResponse(status_code=200, content="Success!")
