from models.User.user import User
from models.Customer.customer import Customer
from models.Address.Address import Address
from models.Phone.phone import Phone
from models.Contract import contract
from models.Customer import customer
from models.Employee import Employee
from models.Financial import Financial
from models.Login import Login
from models.Task import Task
from models.Sales import Sales
from models.Job.Job import Job
from fastapi import FastAPI
from database import conn,cursor
# User
app = FastAPI()

def created(user:User):
    pass
        
        

def login():
    pass

def update():
    pass

def delete():
    pass

# Customer
def created():
    pass

def update():
    pass

def delete(id:int):
    pass

def getting_all():
    pass

def getting_by_id(id:int):
    pass

def getting_by_active():
    pass

def getting_by_sector():
    pass




# Contract
def upload():
    pass

def getting_by_contractor(contractor:str):
    pass

def getting_contracts_by_valid():
    pass

def getting_all():
    pass

def getting_id(id:int):
    pass


def getting_all_by_customer(customer:int):
    pass

# Project
def create():
    pass

def update():
    pass

def delete():
    pass

def getting_by_id(id:int):
    pass

def getting_all():
    pass

def getting_by_name(name:str):
    pass

def getting_by_type(type:str):
    pass

def getting_by_is_finished(finished:bool):
    pass

def getting_by_date():
    pass

# Employee
def created():
    pass

def update():
    pass

def getting_all():
    pass

def getting_by_id(id:int):
    pass

def getting_all_by_name(name:str):
    pass


def getting_all_by_dep(dep:str):
    pass

def getting_all_by_satisfation(satisfation:str):
    pass
# Task

def create():
    pass

def update():
    pass

def Delete():
    pass

def getting_by_status(status:bool):
    pass

def getting_by_date():
    pass

# Financial
def create():
    pass

def update():
    pass

def delete():
    pass

def getting_all():
    pass

def getting_by_id(id:int):
    pass

def getting_by_type(type:str):
    pass

def getting_by_value():
    pass

def getting_by_date():
    pass

# Candidates
def getting_all_candidates():
    pass

def get_candidates_by_id(id:int):
    pass

def getting_candidates_by_approved():
    pass

def create():
    pass

def update():
    pass

def delete():
    pass

#Job
def create():
    pass

def update():
    pass

def delete():
    pass

def getting_all():
    pass

def getting_by_id():
    pass


def getting_by_date_published():
    pass


def getting_by_finish():
    pass

# Sales
def create():
    pass

def update():
    pass

def delete():
    pass

def getting_all():
    pass

def getting_by_id():
    pass

def getting_by_recorrent():
    pass