from pydantic import BaseModel
from typing import Optional


class Cloth(BaseModel):
    name: str
    color: str
    image: str
    user_id: str
    tags: Optional[list] = None
    purchased_year: Optional[int] = None
    brand: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
