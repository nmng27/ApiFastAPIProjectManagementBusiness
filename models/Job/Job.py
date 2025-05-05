from pydantic import BaseModel
from typing import Optional
from datetime import date
from models.Phone import phone as Phone
from models.Customer import customer as Customer
from models.Project import Project
class Candidate(BaseModel):
    id:Optional[int]
    name:str
    mail:str
    phone:Phone
    Age:int
    approved:bool


class Job(BaseModel):
    id:Optional[int]
    tittle:str
    published_date:date
    description:str
    amount_splent:float
    is_finish:bool
    customer:Customer
    project:Project