from pydantic import BaseModel, SkipValidation
from typing import Optional
from datetime import datetime
from PIL.Image import Image


class Cloth(BaseModel):
    name: str
    color: str
    image: str
    tags: Optional[list] = None
    age: Optional[int] = None
    purchased_date: Optional[datetime] = None
    brand: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
