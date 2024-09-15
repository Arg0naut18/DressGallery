from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.routers.cloth_router import router as cloth_router
from src.routers.user_router import router as user_router
from dotenv import load_dotenv
from src.logging import logger


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


@app.get("/ping")
async def ping():
    return JSONResponse(content="Ping successful!", status_code=200)


@app.get("/", response_class=RedirectResponse)
async def root():
    return "/ping"
