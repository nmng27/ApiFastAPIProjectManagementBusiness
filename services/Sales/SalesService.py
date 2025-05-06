from datetime import date
from typing import List
from models.All.models import Sales
from database import session as db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

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

