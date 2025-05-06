from models.All.models import Job
from sqlalchemy.exc import SQLAlchemyError
from typing import List
from sqlalchemy import select
from database import session as db
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
