from models.All.models import Candidate
from sqlalchemy.exc import SQLAlchemyError
from database import session as db
from sqlalchemy import select
from typing import List


class CandidateService():
    def create_candidate(candidate:Candidate):
        try:
            db.add(candidate)
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def update_candidate(id:int, candidate:Candidate):
        try:
            search:Candidate = select(Candidate).where(Candidate.id is id)
            search.approved = candidate.approved
            search.job = candidate.job
            search.job_id = candidate.job_id
            search.mail_address = candidate.mail_address
            search.name = candidate.name
            search.phone_wpp = candidate.phone_wpp
            search.approved = candidate.approved
            db.commit()
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def delete(id:int):
        try:
            search:Candidate = select(Candidate).where(Candidate.id is id)
            db.delete(search)
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_all()->List[Candidate]:
        try:
            search:List[Candidate] = select(Candidate)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_id(id:int)->Candidate:
        try:
            search:Candidate = select(Candidate).where(Candidate.id is id)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_name(name:str)->List[Candidate]:
        try:
            search:List[Candidate] = select(Candidate).where(Candidate.name is name)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()

    def getting_by_approved(approved:bool)->List[Candidate]:
        try:
            search:List[Candidate] = select(Candidate).where(Candidate.approved is approved)
            return search
        except SQLAlchemyError as ex:
            raise ex
        finally:
            db.close()