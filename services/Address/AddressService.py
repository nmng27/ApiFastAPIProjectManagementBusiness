from models.All.models import Address
from database import session as db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
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