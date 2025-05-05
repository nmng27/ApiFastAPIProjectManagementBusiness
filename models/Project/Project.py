from pydantic import BaseModel
from typing import Optional
from datetime import date
from models.Customer import customer as Customer

class Scope(BaseModel):
    id:Optional[int]
    technologies:str
    methodology:str



class Project(BaseModel):
    id:Optional[int]
    name:str
    date_start:date
    type:str
    objective:str
    is_finished:bool
    scope:Scope
    customer:Customer

