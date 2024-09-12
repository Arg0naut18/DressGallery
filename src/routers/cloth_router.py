from fastapi import APIRouter, HTTPException, Request, Depends
from src.util.mongoUtil import MongoUtil
from fastapi.responses import JSONResponse
from src.model.cloth import Cloth
from src.connector import db
from bson import ObjectId
import os
from src.logging import logger

router = APIRouter()
def error_log(e): return f"Error occurred:\t{e}"


mongo_collection = db.get_collection(os.environ["MONGO_OUTFIT_COLLECTION"])
user_collection = db.get_collection(os.environ["MONGO_USER_COLLECTION"])


async def get_current_user(request: Request):
    user_id = request.headers.get('X-User-ID')
    found_users = await MongoUtil.find(user_collection, {"user_id": user_id})
    if not user_id or len(found_users) != 1:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user_id


def format_inputs(name, color, tags, brand, year_of_purchase, user_id):
    filter_dict = {"user_id": user_id}
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
            {"$or": [{"purchased_year": {"$gte": year_of_purchase}}, {"purchased_year": None}]})
    return filter_dict


@router.post("/add/")
async def add_dress(cloth: Cloth, user_id: str = Depends(get_current_user, use_cache=True)):
    try:
        cloth.user_id = user_id
        await MongoUtil.insert(mongo_collection, cloth.model_dump())
        return JSONResponse(status_code=201, content="Success!")
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=400, content=error_log(e))


@router.get("/view/")
async def view_dress(name: str = None, color: str = None, tags: str = None, year_of_purchase: int = None, brand: str = None, user_id: str = Depends(get_current_user, use_cache=True)):
    filter_dict = format_inputs(
        name, color, tags, brand, year_of_purchase, user_id)
    try:
        dresses = await MongoUtil.find(mongo_collection, filter_dict)
        return JSONResponse(content=dresses, status_code=200)
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=400, content=error_log(e))


@router.put("/update/{dress_id}")
async def update_dress(dress_id: str, cloth: Cloth, user_id: str = Depends(get_current_user)):
    updated_dress = cloth.model_dump()
    try:
        await MongoUtil.update(mongo_collection, {'_id': ObjectId(dress_id)}, updated_dress)
        return JSONResponse(status_code=200, content="Success!")
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=400, content=error_log(e))


@router.delete("/delete/{dress_id}")
async def delete_dress(dress_id: str, user_id: str = Depends(get_current_user)):
    try:
        await MongoUtil.delete(mongo_collection, {'_id': ObjectId(dress_id)})
        return JSONResponse(status_code=200, content="Deleted successfully!")
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=400, content=error_log(e))


@router.get("/ping")
async def ping():
    return JSONResponse(content="Cloth Ping successful!", status_code=200)
