from pydantic import BaseModel
from typing import Optional
from models.Customer import customer


class Contract(BaseModel):
    id:Optional[int]
    contractor:customer
    object:str
    obligations:str
    time_valid:int
    is_valid:bool
    termination_remarks:str


