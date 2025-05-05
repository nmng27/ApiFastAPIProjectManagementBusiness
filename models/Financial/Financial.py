from pydantic import BaseModel
from datetime import date
from typing import Optional

class Account(BaseModel):
    id:Optional[int]
    type:str
    value:float
    date_created:date



