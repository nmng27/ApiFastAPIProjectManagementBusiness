from pydantic import BaseModel
from typing import Optional
class Address(BaseModel):
    id:Optional[int]
    street:str
    neighborhood:str
    number:int
    cep:str
