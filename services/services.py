from models.All.models import Address
from database import session as db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.All.models import Phone, Address, User,Customer,Contract,Project,Task,Job,Candidate,FinancialRegistration,Sales
from typing import List
from datetime import date
class AddressService():
    def create(new_address:Address):
        try:
            db.add(new_address)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int, address:Address):
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
    def create(phone:Phone):
        try:
            db.add(phone)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int,phone:Phone):
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
    def create_customer(customer:Customer):
        try:
            db.add(customer)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update_customer(customer:Customer,id:int):
        try:
            search:Customer = select(Customer).where(Customer.id is id)
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
            search:Customer = select(Customer).where(Customer.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    def getting_all_customer()->List[Customer]:
        try:
            customers:List[Customer] = select(Customer)
            return customers
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def getting_customer_by_id(id:int)->Customer:
        try:
            customer:Customer = select(Customer).where(Customer.id is id)
            return customer
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_customer_by_sector(secotr:str)->List[Customer]:
        try:
            customers:List[Customer] = select(Customer).where(Customer.sector == secotr)
            return customers
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_customer_by_service(service:str)->List[Customer]:
        try:
            customers:List[Customer] = select(Customer).where(Customer.service is service)
            return customers
        except SQLAlchemyError as e:
            raise e
        finally:
            db.close()
    

def create_user(user:User):
    try:
        db.add(user)
        db.commit()
    except SQLAlchemyError as ex:
        raise ex
    finally:
        db.close()


def update_user(id:int,user:User):
    try:
        search:User = select(User).where(User.id is id)
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
        search:User = select(User).where(User.id is id)
        db.delete(search)
        db.commit()
    except SQLAlchemyError as e:
        raise e
    finally:
        db.close()
    
    

def login(email:str, pwd:str):
    try:
        search:User = select(User).where(User.mail_addres is email and User.password is pwd)
        if(search):
            return search
        return None
    except SQLAlchemyError as ex:
        raise ex
    finally:
        db.close()

def create_contract(new_contract:Contract):
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
    def create(project:Project):
        try:
            db.add(project)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def update(id:int,project:Project):
        try:
            search:Project = select(project)
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
            search:Project = select(Project).where(Project.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[Project]:
        try:
            projects:List[Project] = select(Project)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Project:
        try:
            project:Project = select(Project).where(Project.id is id)
            return project
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str)->List[Project]:
        try:
            projects:List[Project] = select(Project).where(Project.name is name)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_type(type:str):
        try:
            projects:List[Project] = select(Project).where(Project.type is type)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_is_finished(finished:bool):
        try:
            projects:List[Project] = select(Project).where(Project.is_finished is finished)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class TaskService:
    def create(task:Task):
        try:
            db.add(task)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(task:Task,id:int):
        try:
            search:Task = select(Task).where(Task.id is id)
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
            search:Task = select(Task).where(Task.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def getting_all()->List[Task]:
        try:
            tasks:List[Task] = select(Task)
            return tasks
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Task:
        try:
            task:Task = select(Task).where(Task.id is id)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    
    def getting_by_name(name:str)->List[Task]:
        try:
            task:List[Task] = select(Task).where(Task.name is name)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    
    def getting_by_status(status:bool)->List[Task]:
        try:
            task:List[Task] = select(Task).where(Task.status is status)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()
    
    def getting_by_type(type:str):
        try:
            task:List[Task] = select(Task).where(Task.id is id)
            return task
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class JobService:
    def create(job:Job):
        try:
            db.add(job)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(job:Job,id:int):
        try:
            search:Job = select(Job).where(Job.id is id)
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
            search:Job = select(Job).where(Job.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[Job]:
        try:
            jobs:List[Job] = select(Job)
            return jobs
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Job:
        try:
            search:Job = select(Job).where(Job.id is id)
            return search  
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

def getting_by_name(name:str):
    try:
            search:Job = select(Job).where(Job.name is name)
            return search  
    except SQLAlchemyError as ex:
        raise ex
    finally:
        db.close()

class CandidateService():
    def create_candidate(candidate:Candidate):
        try:
            db.add(candidate)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update_candidate(id:int, candidate:Candidate):
        try:
            search:Candidate = select(Candidate).where(Candidate.id is id)
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
            search:Candidate = select(Candidate).where(Candidate.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[Candidate]:
        try:
            search:List[Candidate] = select(Candidate)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Candidate:
        try:
            search:Candidate = select(Candidate).where(Candidate.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str)->List[Candidate]:
        try:
            search:List[Candidate] = select(Candidate).where(Candidate.name is name)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_approved(approved:bool)->List[Candidate]:
        try:
            search:List[Candidate] = select(Candidate).where(Candidate.approved is approved)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class SalesService():
    def create(new_sale:Sales):
        try:
            db.add(new_sale)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int,sales:Sales):
        try:
            search:Sales = select(Sales).where(Sales.id is id)
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
            search:Sales = select(Sales).where(Sales.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[Sales]:
        try:
            sales:List[Sales] = select(Sales)
            return sales
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Sales:
        try:
            search:Sales = select(Sales).where(Sales.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str):
        try:
            search:List[Sales] = select(Sales).where(Sales.name is name)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def gettting_by_type(type:str):
        try:
            search:List[Sales] = select(Sales).where(Sales.type is type)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_value(value:float):
        try:
            search:List[Sales] = select(Sales).where(Sales.value > value)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_date(date_press:date):
        try:
            search:List[Sales] = select(Sales).where(Sales.date_register is date)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

class FinancialService:
    def create(financial:FinancialRegistration):
        try:
            db.add(financial)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update(id:int,financial:FinancialRegistration):
        try:
            search:FinancialRegistration = select(FinancialRegistration).where(FinancialRegistration.id is id)
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
            search:FinancialRegistration = select(FinancialRegistration.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[FinancialRegistration]:
        try:
            search:List[FinancialRegistration] = select(FinancialRegistration)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->FinancialRegistration:
        try:
            search:FinancialRegistration = select(FinancialRegistration).where(FinancialRegistration.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str)->List[FinancialRegistration]:
        try:
            search:List[FinancialRegistration] = select(FinancialRegistration).where(FinancialRegistration.name is name)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_type(type:str)->List[FinancialRegistration]:
        try:
            search:List[FinancialRegistration] = select(FinancialRegistration).where(FinancialRegistration.type is type)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_value(value:float):
        try:
            search:FinancialRegistration = select(FinancialRegistration).where(FinancialRegistration.value > value)
            return search
        except SQLAlchemyError as e:
            raise e
        finally:
            db.close()

            
