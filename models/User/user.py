from pydantic import BaseModel
from typing import Optional
from models.Address import address
from models.Phone import phone

class User(BaseModel):
    id:Optional[int]
    name:str
    cnpj:str
    mail_commercial:str
    address_txt:address
    phone_txt:phone
    role:str


    