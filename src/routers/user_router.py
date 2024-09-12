from fastapi import APIRouter
from src.util.mongoUtil import MongoUtil
from fastapi.responses import JSONResponse
from src.model.user import User, UserData
from src.connector import db
import os
import uuid
from src.logging import logger
from werkzeug.security import generate_password_hash, check_password_hash
from src.constants import UserUUIDConfig


router = APIRouter()
def error_log(e): return f"Error occurred:\t{e}"


users_collection = db.get_collection(os.environ["MONGO_USER_COLLECTION"])


@router.post("/register/")
async def register_user(user: User):
    user_id = str(uuid.uuid5(UserUUIDConfig.NAMESPACE +
                  str(uuid.uuid4()), user.username))
    hashed_password = generate_password_hash(user.password)

    updated_user = User(user_id=user_id, password=hashed_password,
                        username=user.username, email=user.email, phone_number=user.phone_number)
    try:
        await MongoUtil.insert(users_collection, updated_user.model_dump())
        return JSONResponse(status_code=200, content=user_id)
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=500, content=error_log(e))


@router.post("/login/")
async def authenticate_user(user: UserData):
    curr_user = UserData(username=user.username, email=user.email)
    try:
        users = await MongoUtil.find(
            users_collection, curr_user.model_dump(exclude_unset=True, exclude_none=True))
        user_found = (len(users) > 0)
        if not user_found:
            return JSONResponse(status_code=402, content="User not found!")
        for iter_user in users:
            if check_password_hash(iter_user["password"], user.password):
                return JSONResponse(status_code=200, content=iter_user["user_id"])
        return JSONResponse(status_code=402, content="User not found!")
    except Exception as e:
        logger.error(error_log(e))
        return JSONResponse(status_code=500, content=error_log(e))


@router.get("/ping")
async def ping():
    return JSONResponse(content="User Ping successful!", status_code=200)
