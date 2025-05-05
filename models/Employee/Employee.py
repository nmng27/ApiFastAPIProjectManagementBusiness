from pydantic import BaseModel
from typing import Optional
class Employee():
    id:Optional[int]
    name:str
    corporative_mail:str
    current_job:str
    department:str
    level_satisfation:str
