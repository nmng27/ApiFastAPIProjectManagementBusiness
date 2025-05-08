from database import base as Base
from datetime import date
from sqlalchemy import  Integer, String,Date,Boolean,Float
from sqlalchemy.orm import relationship,Mapped,mapped_column
from typing import List

class Phone(Base):
    __tablename__ = "TB_PHONE"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    ddd:Mapped[int] = mapped_column(Integer)
    number:Mapped[int] = mapped_column(Integer)

    def __repr__(self)->str:
        return f"""
                DDD: {self.ddd}
                Número de Telefone: {self.number}
                """

class Address(Base):
    __tablename__ = "TB_ADDRESS"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    street:Mapped[str] = mapped_column(String(100),nullable=False)
    neighborhood:Mapped[str] = mapped_column(String(100),nullable=False)
    number:Mapped[int] = mapped_column(Integer,nullable=False)
    cep:Mapped[str] = mapped_column(String(8),nullable=False)

    def __repr(self)->str:
        return f"""
            Rua: {self.street}
            Bairro: {self.neighborhood}
            Número: {self.number}
            CEP: {self.cep}
        """
class Customer(Base):
    __tablename__ = "TB_CUSTOMER"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    fantasy_name:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    sector:Mapped[str] = mapped_column(String(100),nullable=False)
    Foundation:Mapped[date] = mapped_column(Date,nullable=False)
    service:Mapped[str] = mapped_column(String(100),nullable=False)

    phone_id:Mapped[int] = mapped_column(Integer,nullable=False)
    phone:Mapped[List[Phone]] = relationship(back_populates="phone_customer")
    address_id:Mapped[int] = mapped_column(Integer,nullable=False)
    address:Mapped[List[Address]] = relationship(back_populates="addresses_customer")

    def __repr__(self)->str:
        return f"""
                Nome Fantasia: {self.fantasy_name}
                Setor: {self.sector}
                Data de fundação: {self.Foundation}
                Tipo de Registro: {self.service}
            """

class User(Base):
    __tablename__ = "TB_USER"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    mail_addres:Mapped[str] = mapped_column(String(100),nullable=False, unique=True)
    date_of_birth:Mapped[date] = mapped_column(Date,nullable=False)
    current_job:Mapped[str] = mapped_column(String(50),nullable=False)
    department:Mapped[str] = mapped_column(String(100),nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customer_user")
    password:Mapped[str] = mapped_column(String(20),nullable=False)
    phone_id:Mapped[int] = mapped_column(Integer,nullable=False)
    phone:Mapped[List[Phone]] = relationship(back_populates="phone")
    address_id:Mapped[int] = mapped_column(Integer,nullable=False)
    address:Mapped[List[Address]] = relationship(back_populates="addresses")

    def __repr__(self)->str:
        return f"""
            Nome:{self.name} 
            Endereço de e-mail:{self.mail_addres} 
            Data de Nascimento: {self.date_of_birth}
            Cargo: {self.current_job}
            Departamento: {self.department}

        """
    



class Contract(Base):
    __tablename__ = "TB_CONTRACT"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    tittle:Mapped[str] = mapped_column(String(200),unique=True,nullable=False)
    date_sign:Mapped[Date] = mapped_column(Date,nullable=False,default=date.today())
    objectives:Mapped[str] = mapped_column(String(100),nullable=False)
    obligations:Mapped[str] = mapped_column(String(100),nullable=False)
    is_valid:Mapped[bool] = mapped_column(Boolean,nullable=False)
    archive: Mapped[str] = mapped_column(String(250),nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customers")

    def __repr__(self)->str:
        return f"""
        Título: {self.tittle}
        Objetivos: {self.objectives}
        Obrigações: {self.obligations}
        Arquivo: {self.archive}
        Contrato está sob vigência: {self.is_valid}
        """

class Project(Base):
    __tablename__ = "TB_PROJECT"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    tech:Mapped[str] = mapped_column(String(200),nullable=False)
    methodology:Mapped[str] = mapped_column(String(100),nullable=False)
    type:Mapped[str] = mapped_column(String(100),nullable=False)
    date_start:Mapped[date] = mapped_column(Date,nullable=False)
    is_finished:Mapped[bool] = mapped_column(Boolean,default=True)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customers_projects")
    contract_id:Mapped[int] = mapped_column(Integer,nullable=False)
    contract:Mapped[List[Contract]] = relationship(back_populates="contracts_project")




    def __repr__(self)->str:
        return f"""
            Nome: {self.name}
            Tipo do projeto: {self.type}
            Data de Inicio: {self.date_start}
            Tecnologias: {self.tech}
            Metodologias: {self.methodology}
            Finalizado: {self.is_finished}
        """


class Task():
    __tablename__ = "TB_TASK"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    type:Mapped[str]= mapped_column(String(100),nullable=False)
    date_task:Mapped[date] = mapped_column(Date,nullable=False)
    status:Mapped[bool] = mapped_column(Boolean,nullable=False)
    project_id:Mapped[int] = mapped_column(Integer,nullable=False)
    project:Mapped[List[Project]] = relationship(back_populates="project_task")
    user_id:Mapped[int] = mapped_column(Integer,nullable=False)
    user:Mapped[List[User]] = relationship(back_populates="user_task")

    def __repr__(self)->str:
        return f"""
            Nome: {self.name}
            Tipo: {self.type}
            Data de Criação: {self.date_task}
            status: {self.status}
            """

class Job():
    __tablename__ = "TB_JOB"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    seniority:Mapped[str]= mapped_column(String(100),nullable=False)
    budget:Mapped[int] = mapped_column()
    search_tool:Mapped[str] = mapped_column(String(100),nullable=False)
    is_checked:Mapped[bool] = mapped_column(Boolean,nullable=False)
    project_id:Mapped[int] = mapped_column(Integer,nullable=False)
    project:Mapped[List[Project]] = relationship(back_populates="project_job")
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customers_job")


class Candidate():
    __tablename__ = "TB_CANDIDATE"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    mail_address:Mapped[str] = mapped_column(String(150),nullable=False,unique=True)
    phone_wpp:Mapped[str] =mapped_column(String(150),nullable=False,unique=True)
    approved:Mapped[bool] = mapped_column(Boolean,nullable=False,unique=True)
    job_id:Mapped[int] = mapped_column(Integer,nullable=False)
    job:Mapped[List[Job]] = relationship(back_populates="job_cand")


class FinancialRegistration():
    __tablename__ = "TB_FINANCIALS"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    type:Mapped[str] = mapped_column(String(100),nullable=False)
    value:Mapped[float] = mapped_column(Float,nullable=False) 
    date_register:Mapped[date] = mapped_column(Date,nullable=False)
    is_recorrent:Mapped[bool] = mapped_column(Boolean, nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customer_financial")
    contract_id:Mapped[int] = mapped_column(Integer,nullable=False)
    contract:Mapped[List[Contract]] = relationship(back_populates="contracts_financial")

class Sales():
    __tablename__ = "TB_SALES"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    type:Mapped[str] = mapped_column(String(100),nullable=False)
    value:Mapped[float] = mapped_column(Float,nullable=False)  
    date_register:Mapped[date] = mapped_column(Date,nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customer_sales")
    