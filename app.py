from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.cloth_router import router as cloth_router
from src.routers.user_router import router as user_router
from dotenv import load_dotenv
import uvicorn
import os
from src.logging import logger, logger_config


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
logger.info('Started!')


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST', '127.0.0.1'),
                port=int(os.getenv('PORT', 8000)), env_file=".env", use_colors=True, log_config=logger_config)
