from models.All.models import User
from database import session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
def create_user(user:User):
    try:
        session.add(user)
        session.commit()
    except SQLAlchemyError as ex:
        raise ex
    finally:
        session.close()


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
        session.commit()
    except SQLAlchemyError as e:
        raise e
    finally:
        session.close()

def delete(id:int):
    try:
        search:User = select(User).where(User.id is id)
        session.delete(search)
        session.commit()
    except SQLAlchemyError as e:
        raise e
    finally:
        session.close()
    
    

def login(email:str, pwd:str):
    try:
        search:User = select(User).where(User.mail_addres is email and User.password is pwd)
        if(search):
            return search
        return None
    except SQLAlchemyError as ex:
        raise ex
    finally:
        session.close()

    