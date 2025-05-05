from pydantic import BaseModel
from typing import Optional
from datetime import date
from models.Address import addressn as Address
from models.Phone import phone as Phone

class Customer(BaseModel):
    id:Optional[int]
    name:str
    mail_address:str
    sector:str
    date_open:date 
    phone:Phone
    address:Address
    active:bool


