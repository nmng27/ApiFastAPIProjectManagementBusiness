from pydantic import BaseModel
from typing import Optional
from datetime import date
from models.Employee import Employee
class Task(BaseModel):
    id:Optional[int]
    tittle:str
    description:str
    date_created:date
    status:bool
    emp:Employee