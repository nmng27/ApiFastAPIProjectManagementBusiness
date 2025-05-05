from pydantic import BaseModel
from typing import Optional
class Phone(BaseModel):
    id:Optional[int]
    ddd:int
    number:int