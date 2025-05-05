from pydantic import BaseModel
from typing import Optional
from models.Customer import customer
class ContractPayment():
    id:Optional[int]
    total_to_pay:float
    is_pay:bool
    type_of_pay:str

class Contract(BaseModel):
    id:Optional[int]
    Payment:ContractPayment
    contractor:customer
    object:str
    obligations:str
    time_valid:int
    is_valid:bool
    termination_remarks:str


