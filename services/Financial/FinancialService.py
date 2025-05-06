from models.All.models import FinancialRegistration
from sqlalchemy.exc import SQLAlchemyError
from database import session as db
from sqlalchemy import select
from typing import List

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

            
