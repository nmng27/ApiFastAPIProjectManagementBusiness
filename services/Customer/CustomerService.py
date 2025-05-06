from database import session as db
from models.All.models import Customer
from sqlalchemy import select
from typing import List
from sqlalchemy.exc import SQLAlchemyError
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
    

