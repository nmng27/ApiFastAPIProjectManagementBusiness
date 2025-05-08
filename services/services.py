from models.All.models import Address
from Schemas.Schema import Address as AddresSchema, PhoneSchema,UserSchema,CustomerSchema,ProjectSchema,TaskSchema,FinancialSchema,SalesSchema,JobSchema,CandidateSchema
from database import session as db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.All.models import Phone, Address, User,Customer,Contract,Project,Task,Job,Candidate,FinancialRegistration,Sales
from typing import List
from datetime import date
class AddressService():
    def create(new_address:AddresSchema):
        try:
            db.add(new_address)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int, address:AddresSchema):
        try:
            search:Address = select(Address).where(Address.id is id)
            search.street = address.street
            search.number = address.number
            search.neighborhood = address.neighborhood
            search.cep = address.cep
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


class PhoneService:
    def create(phone:PhoneSchema):
        try:
            db.add(phone)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int,phone:PhoneSchema):
        try:
            search:Phone = select(Phone.id is id)
            search.ddd = phone.ddd
            search.number = phone.number
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class CustomerService:
    def create_customer(customer:CustomerSchema):
        try:
            db.add(customer)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update_customer(customer:CustomerSchema,id:int):
        try:
            search:CustomerSchema = select(Customer).where(CustomerSchema.id is id)
            search.fantasy_name = customer.fantasy_name
            search.Foundation = customer.Foundation
            search.service = customer.service
            search.phone = customer.phone
            search.phone_id = customer.phone_id
            search.address = customer.address
            search.address_id = customer.address_id
            search.sector = customer.sector
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete_customer(id:int):
        try:
            search:CustomerSchema = select(Customer).where(CustomerSchema.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    def getting_all_customer()->List[CustomerSchema]:
        try:
            customers:List[Customer] = select(Customer)
            return customers
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def getting_customer_by_id(id:int)->CustomerSchema:
        try:
            customer:CustomerSchema = select(Customer).where(Customer.id is id)
            return customer
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_customer_by_sector(secotr:str)->List[CustomerSchema]:
        try:
            customers:List[CustomerSchema] = select(CustomerSchema).where(CustomerSchema.sector == secotr)
            return customers
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_customer_by_service(service:str)->List[CustomerSchema]:
        try:
            customers:List[Customer] = select(CustomerSchema).where(CustomerSchema.service is service)
            return customers
        except SQLAlchemyError as e:
            raise e
        finally:
            db.close()
    

class UserService():
    def create_user(user:UserSchema):
        try:
            db.add(user)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def update_user(id:int,user:UserSchema):
        try:
            search:User = select(User).where(UserSchema.id is id)
            search.name = user.name
            search.mail_addres = user.mail_addres
            search.address_id = user.address_id
            search.address = user.address
            search.phone = user.phone
            search.date_of_birth = user.date_of_birth
            search.current_job = user.current_job
            search.department = user.department
            search.password = user.password
            db.commit()
        except SQLAlchemyError as e:
            raise e
        finally:
            db.close()

    def delete(id:int):
        try:
            search:User = select(UserSchema).where(UserSchema.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as e:
            raise e
        finally:
            db.close()
        
        

    def login(email:str, pwd:str):
        try:
            search:UserSchema = select(UserSchema).where(UserSchema.mail_addres is email and UserSchema.password is pwd)
            if(search):
                return search
            return None
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class ContractService:

    def create_contract(new_contract):
        try:
            db.add(new_contract)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update_contract(id:int,contract:Contract):
        try:
            search:Contract = select(Contract).where(Contract.id is id)
            search.archive = contract.archive
            search.customer = contract.customer
            search.customer_id = contract.customer_id
            search.date_sign = contract.date_sign
            search.is_valid = contract.is_valid
            search.objectives = contract.objectives
            search.obligations = contract.obligations
            search.tittle = contract.tittle
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_contract_by_id(id:int)->Contract:
        try:
            search:Contract = select(Contract).where(Contract.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_contract_by_valid(valid:bool)->List[Contract]:
        try:
            search:Contract = select(Contract).where(Contract.is_valid is valid)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_contract_by_customer(customer:int):
        try:
            search:List[Contract] = select(Contract).where(Contract.customer_id is customer)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_contract()->List[Contract]:
        try:
            contracts:List[Contract] = select(Contract)
            return contracts
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


class ProjectService:
    def create(project:ProjectSchema):
        try:
            db.add(project)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def update(id:int,project:ProjectSchema):
        try:
            search:ProjectSchema = select(project)
            search.type = project.type
            search.tech = project.tech
            search.methodology = project.methodology
            search.contract = project.contract
            search.contract_id = project.contract_id
            search.customer = project.customer
            search.customer_id = project.customer_id
            search.is_finished = project.is_finished
            search.date_start = project.date_start
            search.name = project.name
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:ProjectSchema = select(ProjectSchema).where(ProjectSchema.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[ProjectSchema]:
        try:
            projects:List[ProjectSchema] = select(ProjectSchema)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->ProjectSchema:
        try:
            project:ProjectSchema = select(Project).where(ProjectSchema.id is id)
            return project
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str)->List[ProjectSchema]:
        try:
            projects:List[ProjectSchema] = select(ProjectSchema).where(ProjectSchema.name is name)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_type(type:str):
        try:
            projects:List[ProjectSchema] = select(ProjectSchema).where(ProjectSchema.type is type)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_is_finished(finished:bool):
        try:
            projects:List[ProjectSchema] = select(ProjectSchema).where(ProjectSchema.is_finished is finished)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class TaskService:
    def create(task:TaskSchema):
        try:
            db.add(task)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(task:TaskSchema,id:int):
        try:
            search:TaskSchema = select(TaskSchema).where(TaskSchema.id is id)
            search.date_task = task.date_task
            search.name = task.name
            search.status = task.status
            search.project = task.project
            search.project_id = task.project_id
            search.type = task.type
            search.date_task = task.date_task
            search.user = task.user
            search.user_id = task.user_id
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def delete(id:int):
        try:
            search:TaskSchema = select(TaskSchema).where(TaskSchema.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def getting_all()->List[Task]:
        try:
            tasks:List[TaskSchema] = select(TaskSchema)
            return tasks
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->TaskSchema:
        try:
            task:Task = select(TaskSchema).where(TaskSchema.id is id)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    
    def getting_by_name(name:str)->List[TaskSchema]:
        try:
            task:List[TaskSchema] = select(TaskSchema).where(TaskSchema.name is name)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    
    def getting_by_status(status:bool)->List[TaskSchema]:
        try:
            task:List[TaskSchema] = select(TaskSchema).where(TaskSchema.status is status)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    
   

class JobService:
    def create(job:JobSchema):
        try:
            db.add(job)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(job:JobSchema,id:int):
        try:
            search:Job = select(Job).where(JobSchema.id is id)
            search.customer = job.customer
            search.budget = job.budget
            search.customer_id = job.customer_id
            search.is_checked = job.is_checked
            search.name = job.name
            search.seniority = job.seniority
            search.search_tool = job.search_tool
            search.customer_id = job.customer_id
            search.project = job.project
            search.project_id = job.project_id
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:JobSchema = select(JobSchema).where(JobSchema.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[JobSchema]:
        try:
            jobs:List[JobSchema] = select(JobSchema)
            return jobs
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->JobSchema:
        try:
            search:JobSchema = select(Job).where(Job.id is id)
            return search  
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

def getting_by_name(name:str):
    try:
            search:JobSchema = select(Job).where(Job.name is name)
            return search  
    except SQLAlchemyError as ex:
        raise ex
    finally:
        db.close()

class CandidateService():
    def create_candidate(candidate:CandidateSchema):
        try:
            db.add(candidate)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update_candidate(id:int, candidate:CandidateSchema):
        try:
            search:CandidateSchema = select(Candidate).where(Candidate.id is id)
            search.approved = candidate.approved
            search.job = candidate.job
            search.job_id = candidate.job_id
            search.mail_address = candidate.mail_address
            search.name = candidate.name
            search.phone_wpp = candidate.phone_wpp
            search.approved = candidate.approved
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:CandidateSchema = select(Candidate).where(Candidate.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[CandidateSchema]:
        try:
            search:List[Candidate] = select(Candidate)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->CandidateSchema:
        try:
            search:Candidate = select(Candidate).where(Candidate.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    

class SalesService():
    def create(new_sale:SalesSchema):
        try:
            db.add(new_sale)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int,sales:Sales):
        try:
            search:SalesSchema = select(Sales).where(Sales.id is id)
            search.customer = sales.customer
            search.customer_id = sales.customer_id
            search.date_register = sales.date_register
            search.name = sales.name
            search.type = sales.type
            search.value = sales.value
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:SalesSchema = select(Sales).where(Sales.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[SalesSchema]:
        try:
            sales:List[SalesSchema] = select(Sales)
            return sales
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->SalesSchema:
        try:
            search:SalesSchema = select(Sales).where(Sales.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()



class FinancialService:
    def create(financial:FinancialSchema):
        try:
            db.add(financial)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int,financial:FinancialSchema):
        try:
            search:FinancialSchema = select(FinancialRegistration).where(FinancialRegistration.id is id)
            search.contract = financial.contract
            search.contract_id = financial.contract_id
            search.customer = financial.customer
            search.customer_id = financial.customer_id
            search.date_register = financial.date_register
            search.is_recorrent = financial.is_recorrent
            search.name = financial.name
            search.type = financial.type
            search.value = financial.value
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:FinancialSchema = select(FinancialRegistration.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[FinancialRegistration]:
        try:
            search:List[FinancialSchema] = select(FinancialRegistration)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->FinancialSchema:
        try:
            search:FinancialSchema = select(FinancialRegistration).where(FinancialRegistration.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()




            
