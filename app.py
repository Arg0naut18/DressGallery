from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.cloth_router import router as cloth_router
from src.routers.user_router import router as user_router
from dotenv import load_dotenv
from src.logging.logger import logger


load_dotenv()
app = FastAPI()
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
app.include_router(cloth_router, prefix="/outfit")
app.include_router(user_router, prefix="/auth")
logger.debug("Started!")
