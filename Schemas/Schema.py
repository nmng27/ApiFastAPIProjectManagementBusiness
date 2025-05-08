from pydantic import BaseModel, Field, validator, EmailStr
from datetime import date

class Address(BaseModel):
    id:int
    street:str
    neighborhood:str
    number:int = Field(min_length=1, max_length=5,description="Por favor preencha o numero da sua residencia corretamente")
    cep:str = Field(min_length=8,max_length=10,description="Por favor preencha o campo CEP corretamente!")
    
class PhoneSchema(BaseModel):
    id:int
    ddd:int = Field(max_length=2,description="O campo DDD deve ter apenas 2 digitos.")
    number:int = Field(min_length=8,max_length=9, description="O campo de telefone deve ter até 9 digitos")

   



class CustomerSchema(BaseModel):
    id:int
    fantasy_name:str = Field(min_length=5,description="Por fvo preencha o nome fantasia corretamente")
    foundation:date = Field(default=date.today())
    sector:str = Field(min_length=6,description="O campo setor deve ser preenchido corretamente.") 
    service:str = Field(min_length=6,description="O campo setor deve ser preenchido corretamente.") 
    phone_id:int
    address_id:int


    
    


class UserSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    mail_address:EmailStr = Field(min_length=20,description="O campo e-mail deve ser preenchido corretamente.") 
    phone_id:int
    customer_id:int
    address_id:int
    current_job:str =Field(min_length=8,description="O campo cargo atual deve ser preenchido corretamente.") 
    department:str = Field(min_length=8,description="O campo departamento deve ser preenchido corretamente.") 
    password:str = Field(min_length=8,max_length=20,description="Por favor preencha o campo senha corretamente.")

    

class ContractSchema(BaseModel):
    id:int
    tittle:str = Field(min_length=8,description="O campo titulo deve ser preenchido corretamente.") 
    date_sign:date
    objectives:str = Field(min_length=8,description="O campo objetivos deve ser preenchido corretamente.") 
    obligations:str = Field(min_length=8,description="O campo obligations deve ser preenchido corretamente.") 
    is_valid:bool
    archive:str
    customer_id:int

class ProjectSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    tech:str = Field(min_length=8,description="O campo tecnologias deve ser preenchido corretamente.") 
    methodology:str = Field(min_length=8,description="O campo metodologias deve ser preenchido corretamente.") 
    type:str = Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    date_start:date
    is_finished:bool
    customer_id:int
    contract_id:int



    @validator("methodology")
    def meth_validator(cls,v):
        meths = ["Waterfall","PMBOK","PRINCE2","SCRUM","KANBAN","LEAN","XP"]
        if v in meths:
            raise ValueError("A metodologia não é permitida a ser adicionada.")
        return v

    

class TaskSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    type:str =Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    date_created:date
    status:bool
    project_id:int
    customer_id:int


    

class JobSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    seniority:str =Field(min_length=8,description="O campo senioridade deve ser preenchido corretamente.") 
    budget:float 
    search_tool:str = Field(min_length=8,description="O campo ferramenta de busca deve ser preenchido corretamente.") 
    is_checked:bool 
    project_id:int
    customer_id:int

    

class CandidateSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    mail_address:str = Field(min_length=8,description="O campo e-mail deve ser preenchido corretamente.") 
    phone_id:int
    approved:bool
    job_id:int

    

class SalesSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    type:str = Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    value:float
    date_register:date
    customer_id:int

    

class FinancialSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    type:str = Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    value:float
    date_register:date
    is_recorrent:bool
    customer_id:int
    contract_id:int

    


