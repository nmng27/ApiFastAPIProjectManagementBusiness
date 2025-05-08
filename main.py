from models.All.models import Address, Phone,Customer, User, Contract,Project, Task,Job,Candidate,FinancialRegistration,Sales
from Schemas.Schema import Address as AddressSchema, PhoneSchema,CustomerSchema, UserSchema, ContractSchema,ProjectSchema, TaskSchema,JobSchema,CandidateSchema,FinancialSchema,SalesSchema
from services.services import AddressService, PhoneService,CustomerService, UserService, ContractService,ProjectService, TaskService,JobService,CandidateService,FinancialService,SalesService
from fastapi import FastAPI, HTTPException,status
from typing import List
app = FastAPI()

@app.post("/address",response_model=AddressSchema,status_code=status.HTTP_200_OK)
def create_address(addres:Address):
    try:
        AddressService.create(Address)
        return {"status":"Endereço Adicionado com Sucesso!"}
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.put("/address/{id}",response_model=AddressSchema,status_code=status.HTTP_200_OK)
def update_address(new_address:Address,id:int):
    try:
        AddressService.update(id,new_address)
        return {
            "status":"Endereço Atualizado com Sucesso!"
        }
        
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível atualizar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

    
@app.post("/phone",response_model=PhoneSchema,status_code=status.HTTP_200_OK)
def create_phone(phone:Phone):
    try:
        PhoneService.create(phone)
        return {
            "status":"Telefone Adicionado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um telefone.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

    
@app.put("/phone/{id}",response_model=PhoneSchema,status_code=status.HTTP_200_OK)
def update_phone(id:int, phone:Phone):
    try:
        PhoneService.update(id,phone)
        return {
            "status":"Telefone alterado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um telefone.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.post("/customers", response_model=CustomerSchema,status_code=status.HTTP_200_OK)
def create_customer(customer:Customer):
    try:
        CustomerService.create_customer(customer)
        return {
            "status":"Cliente criado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um cliente.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.put("/customers/{id}",response_model=CustomerSchema,status_code=status.HTTP_200_OK)
def update_customer(id:int, customer:Customer):
    try:
        CustomerService.update_customer(id, customer)
        return {
            "status":"Cliente Atualizado com Sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um cliente.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.delete("/customers/{id}",response_model=CustomerSchema,status_code=status.HTTP_200_OK)
def delete(id:int):
    try:
        CustomerService.delete_customer(id)
        return {
            "status":"Dados do cliente excluidos com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.get("/customers",response_model=List[CustomerSchema],status_code=status.HTTP_200_OK)
def listing_customers():
    try:
        customers:List[Customer] = CustomerService.getting_all_customer()
        return customers
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/customer/{id}",response_model=CustomerSchema,status_code=status.HTTP_200_OK)
def getting_customer_by_id(id:int):
    try:
        customer:Customer = CustomerService.getting_customer_by_id(id)
        return customer
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    

@app.get("/customers/{sector}",response_model=List[CustomerSchema],status_code=status.HTTP_200_OK)
def getting_customers_by_sector(sector:str):
    try:
        customers:List[Customer] = CustomerService.getting_customer_by_sector(sector)
        return customers
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    

@app.get("/customers/{service}",response_model=List[CustomerSchema],status_code=status.HTTP_200_OK)
def getting_customers_by_service(service:str):
    try:
        customers:List[Customer] = CustomerService.getting_customer_by_service(service)
        return customers
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    

@app.post("/user",response_model=UserSchema,status_code=status.HTTP_200_OK)
def create_user(user:User):
    try:
        UserService.create_user(user)
        return {
            "status":"Usuário criado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.put("/user/{id}",response_model=UserSchema,status_code=status.HTTP_200_OK)
def update_user(id:int, user:User):
    try:
        UserService.update_user(id,user)
        return {
            "status":"Usuário ATualizado com Sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    

@app.delete("/user/{id}")
def delete_user(id:int):
    try:
        UserService.delete(id)
        return {
            "status":"Usuário deletado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    

@app.post("/login")
def login():
    pass

@app.post("/contract", response_model=ContractSchema,status_code=status.HTTP_200_OK)
def create_contract(contract:Contract):
    try:
        ContractService.create_contract(contract)
        return {
            "status":"Contrato Adicionado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.put("/contract/{id}",response_model=ContractSchema,status_code=status.HTTP_200_OK)
def update_contract(id:int, contract:Contract):
    try:
        ContractService.update_contract(id,contract)
        return {
            "status":"Os dados do contrato foram editado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/contracts", response_model=List[ContractSchema],status_code=status.HTTP_200_OK)
def getting_all_contracts():
    try:
        contracts:List[Contract]=ContractService.getting_contract()
        return contracts
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.get("/contract/{id}",response_model=ContractSchema,status_code=status.HTTP_200_OK)
def getting_contract_by_id(id:int):
    try:
        contract:Contract = ContractService.getting_contract_by_id(id)
        return contract
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.get("/contracts/{valid}",response_model=List[Contract],status_code=status.HTTP_200_OK)
def getting_all_by_validation(valid:bool):
    try:
        contracts:List[Contract]=ContractService.getting_contract_by_valid(valid)
        return contracts
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/contracts/{customer}",response_model=List[Contract],status_code=status.HTTP_200_OK)
def getting_contracts_by_customer(customer:int):
    try:
        contracts:List[Contract] = ContractService.getting_contract_by_customer(customer)
        return contracts
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um endereço.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.post("/projects",response_model=ProjectSchema,status_code=status.HTTP_200_OK)
def create_project(project:Project):
    try:
        ProjectService.create(project)
        return {
            "status":"Projeto criado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.put("/projects/{id}",)
def update_project(id:int,project:Project,response_model=ProjectSchema,status_code=status.HTTP_200_OK):
    try:
        ProjectService.update(id,project)
        return {
            "status":"Projeto atualizado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
    
@app.delete("/projects/{id}")
def delete_project(id:int):
    try:
        ProjectService.delete(id)
        return {
            "status":"Projeto deletado com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/projects",response_model=List[ProjectSchema],status_code=status.HTTP_200_OK)
def getting_all_projects():
    try:
        projects:List[Project] = ProjectService.getting_all()
        return projects
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/projects/{id}", response_model=ProjectSchema,status_code=status.HTTP_200_OK)
def getiing_project_by_id(id:int):
    try:
        project:Project = ProjectService.getting_by_id(id)
        return project
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")



@app.get("/projects/{is_finished}",response_model=ProjectSchema,status_code=status.HTTP_200_OK)
def getting_projects_is_finished(is_finished:bool):
    try:
        projects:List[Project] = ProjectService.getting_by_is_finished(is_finished)
        return projects
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.post("/tasks",response_model=TaskSchema,status_code=status.HTTP_200_OK)
def create_task(task:Task):
    try:
        TaskService.create(task)
        return {
            "status":"Task criada com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar uma task.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.put("/tasks/{id}",response_model=TaskSchema,status_code=status.HTTP_200_OK)
def update_task(id:int,task:Task):
    try:
        TaskService.update(id, task)
        return {
            "status":"Task atualizada com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um task.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.delete("/task/{id}",response_model=TaskSchema,status_code=status.HTTP_200_OK)
def delete_task_by_id(id:int):
    try:
        TaskService.delete(id)
        return {
            "status":"Task excluida com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/tasks",response_model=List[TaskSchema],status_code=status.HTTP_200_OK)
def get_tasks():
    try:
        tasks:List[Task] = TaskService.getting_all()
        return tasks
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.get("/tasks/{id}",response_model=TaskSchema,status_code=status.HTTP_200_OK)
def getting_task_by_id(id:int):
    try:
        task:Task = TaskService.getting_by_id(id)
        return task
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.get("/tasks/{status}")
def getting_task_by_status(status:bool):
    try:
        tasks:List[Task] = TaskService.getting_by_status(status)
        return tasks
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.post("/jobs",response_model=JobSchema,status_code=status.HTTP_200_OK)
def create_job(job:Job):
    try:
        JobService.create(job)
        return {
             "status":"A vaga foi cadastrada com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.put("/jobs/{id}",response_model=JobSchema,status_code=status.HTTP_200_OK)
def update_job(job:Job,id:int):
    try:
        JobService.update(id,job)
        return {
             "status":"Vaga atualizada com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.delete("/jobs/{id}",response_model=JobSchema,status_code=status.HTTP_200_OK)
def delet_job(job:Job):
    try:
        JobService.delete(id)
        return {
             "status":"Cargo excluído com sucesso!"
        }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/jobs",response_model=List[JobSchema],status_code=status.HTTP_200_OK)
def getting_jobs():
    try:
        jobs:List[Job] = JobService.getting_all()
        return jobs
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/jobs",response_model=JobSchema,status_code=status.HTTP_200_OK)
def getting_job_by_id(id:int):
    try:
        job:Job = JobService.getting_by_id(id)
        return job
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.post("/candidates",response_model=CandidateSchema,status_code=status.HTTP_200_OK)
def create_candidate(candidate:Candidate):
    try:
          CandidateService.create_candidate(candidate)
          return {
               "status":"Candidato criado com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.put("/candidates/{id}")
def update_candidate(candidate:Candidate,id:int):
    try:
          CandidateService.update_candidate(candidate)
          return {
               "status":"Candidato atualizado com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")


@app.delete("/candidates/{id}")
def delete_candidate(id:int):
    try:
          CandidateService.delete(id)
          return {
               "status":"Candidato excluído com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/candidates/",response_model=List[CandidateSchema],status_code=status.HTTP_200_OK)
def getting_all_candidates():
    try:
          candidates:List[Candidate] = CandidateService.getting_all()
          return candidates
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/candidates/{id}")
def getting_all_candidates(id:int):
    try:
          candidate:Candidate = CandidateService.getting_by_id(id)
          return candidate
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.post("/finbancial",response_model=FinancialSchema,status_code=status.HTTP_200_OK)
def create_financial_registration(financial:FinancialRegistration):
    try:
          FinancialService.create(financial)
          return {
               "status":"Registro Financeiro criado com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.put("/finbancial/{id}",response_model=FinancialSchema,status_code=status.HTTP_200_OK)
def create_financial_registration(financial:FinancialRegistration,id:int):
    try:
          FinancialService.update(financial,id)
          return {
               "status":"Registro Financeiro atualizado com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.delete("/financial/{id}",response_model=FinancialSchema,status_code=status.HTTP_200_OK)
def create_financial_registration(id:int):
    try:
          FinancialService.delete(id)
          return {
               "status":"Registro Financeiro deletado com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/financials",response_model=List[FinancialRegistration],status_code=status.HTTP_200_OK)
def getting_all_financial_registration():
    try:
        financials:List[FinancialRegistration] = FinancialService.getting_all()
        return financials   
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/financial/{id}",response_model=FinancialSchema,status_code=status.HTTP_200_OK)
def getting_financial_by_id(id:int):
    try:
          financial:FinancialRegistration = FinancialService.getting_by_id(id)
          return financial
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.post("/sales",response_model=SalesSchema,status_code=status.HTTP_200_OK )
def create_sales(sales:Sales):
    try:
          SalesService.create(sales)
          return {
               "status":"Venda criada com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.put("/sales/{id}", response_model=SalesSchema,status_code=status.HTTP_200_OK)
def update_sales(sales:Sales,id:int):
    try:
          SalesService.update(sales)
          return {
               "status":"Venda Atualizada com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.delete("/sales/{id}", response_model=SalesSchema,status_code=status.HTTP_200_OK)
def delete_sales(id:int):
    try:
          SalesService.delete(id)
          return {
               "status":"Venda excluida com sucesso!"
          }
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/sales/{id}", response_model=SalesSchema,status_code=status.HTTP_200_OK)
def get_sales_by_id(id:int):
    try:
          sale:Sales = SalesService.getting_by_id(id)
          return sale
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")

@app.get("/sales",response_model=List[SalesSchema],status_code=status.HTTP_200_OK)
def getting_all_sales():
    try:
          sales:List[Sales] = SalesService.getting_all()
          return sales
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Não é possível adicionar um projeto.")
    except HTTPException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Algo deu errado, verifique se os dados estão inseridos corretamente.")
