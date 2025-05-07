from models.All.models import Phone
from database import session as db
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
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

