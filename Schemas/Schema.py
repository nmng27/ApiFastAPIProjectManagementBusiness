from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Address(BaseModel):
    id:Optional[int]
    street:str
    neighborhood:str
    number:int
    cep:str = Field(min_length=8,max_length=10,description="Por favor preencha o campo CEP corretamente!")
    
class PhoneSchema(BaseModel):
    id:int
    ddd:int
    number:int

class CustomerSchema(BaseModel):
    id:int
    fantasy_name:str
    foundation:date
    sector:str
    service:str
    phone_id:int
    address_id:int

class UserSchema(BaseModel):
    id:int
    name:str
    mail_address:str
    phone_id:int
    customer_id:int
    address_id:int
    current_job:str
    department:str
    password:str

class ContractSchema(BaseModel):
    id:int
    tittle:str
    date_sign:date
    objectives:str
    obligations:str
    is_valid:bool
    archive:str
    customer_id:int

class ProjectSchema(BaseModel):
    id:int
    name:str
    tech:str
    methodology:str
    type:str
    date_start:date
    is_finished:bool
    customer_id:int
    contract_id:int

class TaskSchema(BaseModel):
    id:int
    name:str
    type:str
    date_created:date
    status:bool
    project_id:int
    customer_id:int

class JobSchema(BaseModel):
    id:int
    name:str
    seniority:str
    budget:float
    search_tool:str
    is_checked:bool
    project_id:int
    customer_id:int

class CandidateSchema(BaseModel):
    id:int
    name:str
    mail_address:str
    phone_id:int
    approved:bool
    job_id:int

class SalesSchema(BaseModel):
    id:int
    name:str
    type:str
    value:float
    date_register:date
    customer_id:int

class FinancialSchema(BaseModel):
    id:int
    name:str
    type:str
    value:float
    date_register:date
    is_recorrent:bool
    customer_id:int
    contract_id:int







