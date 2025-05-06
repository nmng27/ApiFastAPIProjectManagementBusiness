from sqlalchemy import select
from models.All.models import Task
from sqlalchemy.exc import SQLAlchemyError
from database import session as db
from typing import List

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