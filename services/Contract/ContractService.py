from models.All.models import Contract
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from database import session as db
from sqlalchemy import select
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