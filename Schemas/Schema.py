from pydantic import BaseModel

class UserSchema:
    pass



class CustomerSchema:
    pass

class ProjectSchema:
    pass

class ContractSchema:
    pass

class Task:
    pass

class JobSchema:
    pass

class CandidateSchema:
    pass

class Financial:
    pass

class SalesSchema:
    pass

class PhoneSchema:
    id:int
    ddd:str
    number:str

class Address(BaseModel):
    id:int
    street:str
    neighborhood:str
    number:int
    cep:str

