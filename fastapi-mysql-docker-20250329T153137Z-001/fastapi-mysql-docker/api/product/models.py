from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    id:  Optional[int] = None
    IceCreamName: str
    ToppingName: str
    Price: float
    Size: str