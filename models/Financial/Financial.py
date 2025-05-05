from pydantic import BaseModel
from datetime import date
from typing import Optional

class Account(BaseModel):
    id:Optional[int]
    type:str
    value:float
    date_created:date 


class Financial:
    id:Optional[int]
    total_revenue:float
    total_expense:float
    balance:int
    status:str
    account:Account
