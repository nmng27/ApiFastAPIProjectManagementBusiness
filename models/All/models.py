from database import session, engine,base as Base
from datetime import date
from sqlalchemy import Column, Integer, String,Date,Boolean
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


class User(Base):
    __tablename__ = "TB_USER"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(100),nullable=False)
    mail_addres:Mapped[str] = mapped_column(String(100),nullable=False, unique=True)
    date_of_birth:Mapped[date] = mapped_column(Date,nullable=False)
    current_job:Mapped[str] = mapped_column(String(50),nullable=False)
    department:Mapped[str] = mapped_column(String(100),nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer = relationship(back_populates="customer_user",cascade="all, delete-orphan")
    password:Mapped[str] = mapped_column(String(20),nullable=False)
    phone_id:Mapped[int] = mapped_column(Integer,nullable=False)
    phone:List[Phone] = relationship(back_populates="phone",cascade="all, delete-orphan")
    address_id:Mapped[int] = mapped_column(Integer,nullable=False)
    address:Mapped[List[Address]] = relationship(back_populates="addresses",cascade="all, delete-orphan")

    def __repr__(self)->str:
        return f"""
            Nome:{self.name} 
            Endereço de e-mail:{self.mail_addres} 
            Data de Nascimento: {self.date_of_birth}
            Cargo: {self.current_job}
            Departamento: {self.department}

        """
    

class Customer(Base):
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    fantasy_name:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    sector:Mapped[str] = mapped_column(String(100),nullable=False)
    Foundation:Mapped[date] = mapped_column(Date,nullable=False)
    service:Mapped[str] = mapped_column(String(100),nullable=False)

    phone_id:Mapped[int] = mapped_column(Integer,nullable=False)
    phone:Mapped[List[Phone]] = relationship(back_populates="phone_customer",cascade="all, delete-orphan")
    address_id:Mapped[int] = mapped_column(Integer,nullable=False)
    address:Mapped[List[Address]] = relationship(back_populates="addresses_customer",cascade="all, delete-orphan")

    def __repr__(self)->str:
        return f"""
                Nome Fantasia: {self.fantasy_name}
                Setor: {self.sector}
                Data de fundação: {self.Foundation}
                Tipo de Registro: {self.service}
            """

class Contract(Base):
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    tittle:Mapped[str] = mapped_column(String(200),unique=True,nullable=False)
    date_sign:Mapped[Date] = mapped_column(Date,nullable=False,default=date.today())
    objectives:Mapped[str] = mapped_column(String(100),nullable=False)
    obligations:Mapped[str] = mapped_column(String(100),nullable=False)
    is_valid:Mapped[bool] = mapped_column(Boolean,nullable=False)
    archive: Mapped[str] = mapped_column(String(250),nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customers",cascade="all, delete-orphan")

    def __repr__(self)->str:
        return f"""
        Título: {self.tittle}
        Objetivos: {self.objectives}
        Obrigações: {self.obligations}
        Arquivo: {self.archive}
        Contrato está sob vigência: {self.is_valid}
        """

class Project(Base):
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    tech:Mapped[str] = mapped_column(String(200),nullable=False)
    methodology:Mapped[str] = mapped_column(String(100),nullable=False)
    type:Mapped[str] = mapped_column(String(100),nullable=False)
    date_start:Mapped[date] = mapped_column(Date,nullable=False)
    is_finished:Mapped[bool] = mapped_column(Boolean,default=True)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customers_projects",cascade="all, delete-orphan")
    contract_id:Mapped[int] = mapped_column(Integer,nullable=False)
    contract:Mapped[List[Contract]] = relationship(back_populates="contracts_project",cascade="all, delete-orphan")




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
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    type:Mapped[str]= mapped_column(String(100),nullable=False)
    date_task:Mapped[date] = mapped_column(Date,nullable=False)
    status:Mapped[bool] = mapped_column(Boolean,nullable=False)
    project_id:Mapped[int] = mapped_column(Integer,nullable=False)
    project:Mapped[List[Project]] = relationship(back_populates="project_task",cascade="all, delete-orphan")
    user_id:Mapped[int] = mapped_column(Integer,nullable=False)
    user:Mapped[List[User]] = relationship(back_populates="user_task",cascade="all delete-orphan")

    def __repr__(self)->str:
        return f"""
            Nome: {self.name}
            Tipo: {self.type}
            Data de Criação: {self.date_task}
            status: {self.status}
            """

class Job():
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    seniority:Mapped[str]= mapped_column(String(100),nullable=False)
    budget:Mapped[int] = mapped_column()
    search_tool:Mapped[str] = mapped_column(String(100),nullable=False)
    is_checked:Mapped[bool] = mapped_column(Boolean,nullable=False)
    project_id:Mapped[int] = mapped_column(Integer,nullable=False)
    project:Mapped[List[Project]] = relationship(back_populates="project_job",cascade="all, delete-orphan")
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customers_job",cascade="all, delete-orphan")


class Candidate():
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    mail_address:Mapped[str] = mapped_column(String(150),nullable=False,unique=True)
    phone_wpp:Mapped[str] =mapped_column(String(150),nullable=False,unique=True)
    approved:Mapped[bool] = mapped_column(Boolean,nullable=False,unique=True)
    job_id:Mapped[int] = mapped_column(Integer,nullable=False)
    job:Mapped[List[Job]] = relationship(back_populates="job_cand",cascade="all delete-orphan ")


class FinancialRegistration():
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    type:Mapped[str] = mapped_column(String(100),nullable=False)
    value:Mapped[float] = None 
    date_register:Mapped[date] = mapped_column(Date,nullable=False)
    is_recorrent:Mapped[bool] = mapped_column(Boolean, nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customer_financial",cascade="all delete-orphan")
    contract_id:Mapped[int] = mapped_column(Integer,nullable=False)
    contract:Mapped[List[Contract]] = relationship(back_populates="contracts_financial",cascade="all delete-orphan")

class Sales():
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]= mapped_column(String(100),nullable=False)
    type:Mapped[str] = mapped_column(String(100),nullable=False)
    value:Mapped[float] = None 
    date_register:Mapped[date] = mapped_column(Date,nullable=False)
    customer_id:Mapped[int] = mapped_column(Integer,nullable=False)
    customer:Mapped[List[Customer]] = relationship(back_populates="customer_sales",cascade="all delete-orphan")
    