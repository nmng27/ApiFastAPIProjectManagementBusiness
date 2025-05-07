from models.All.models import Project
from sqlalchemy import select
from typing import List
from database import session as db
from sqlalchemy.exc import SQLAlchemyError

class ProjectService:
    def create(project:Project):
        try:
            db.add(project)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()


    def update(id:int,project:Project):
        try:
            search:Project = select(project)
            search.type = project.type
            search.tech = project.tech
            search.methodology = project.methodology
            search.contract = project.contract
            search.contract_id = project.contract_id
            search.customer = project.customer
            search.customer_id = project.customer_id
            search.is_finished = project.is_finished
            search.date_start = project.date_start
            search.name = project.name
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:Project = select(Project).where(Project.id is id)
            db.delete(search)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[Project]:
        try:
            projects:List[Project] = select(Project)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Project:
        try:
            project:Project = select(Project).where(Project.id is id)
            return project
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str)->List[Project]:
        try:
            projects:List[Project] = select(Project).where(Project.name is name)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_type(type:str):
        try:
            projects:List[Project] = select(Project).where(Project.type is type)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_is_finished(finished:bool):
        try:
            projects:List[Project] = select(Project).where(Project.is_finished is finished)
            return projects
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

