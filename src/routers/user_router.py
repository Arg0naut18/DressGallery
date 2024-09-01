from fastapi import APIRouter
from src.util.mongoUtil import MongoUtil
from fastapi.responses import JSONResponse
from src.model.user import User
from src.connector import db
from bson import ObjectId
import os
import uuid
from src.logging.logger import logger
from werkzeug.security import generate_password_hash


router = APIRouter()
error_log = lambda e: f"Error occurred! \n{e}"
users_collection = db.get_collection(os.environ["MONGO_USER_COLLECTION"])

@router.post("/register/")
async def register_user(username, password):
    user_id = str(uuid.uuid4())
    hashed_password = generate_password_hash(password)

    user = User(user_id=user_id, password=hashed_password, username=username)
    try:
        MongoUtil.insert(users_collection, user.model_dump())
        return JSONResponse(status_code=200, content=user_id)
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=500, content=error_log(e))


@router.get("/authenticate/")
async def authenticate_user(username, password):
    curr_user = User(username=username, password=generate_password_hash(password))
    try:
        users = MongoUtil.find(users_collection, curr_user.model_dump(exclude_unset=True))
        user_found = (len(users)>0)
        if not user_found:
            return JSONResponse(status_code=402, content="User not found!")
        return JSONResponse(status_code=200, content=users[0].user_id)
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=500, content=error_log(e))
