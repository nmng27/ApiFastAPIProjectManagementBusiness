from pydantic import BaseModel
from models.Customer import customer as Customer
from datetime import date
from typing import Optional

class Sales(BaseModel):
    id:Optional[int]
    date_created:date 
    type:str
    value:float
    is_recorrent:bool
    customer:Customer

