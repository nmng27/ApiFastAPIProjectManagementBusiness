from pydantic import BaseModel, Field, validator, EmailStr
from datetime import date

class Address(BaseModel):
    id:int
    street:str
    neighborhood:str
    number:int = Field(min_length=1, max_length=5,description="Por favor preencha o numero da sua residencia corretamente")
    cep:str = Field(min_length=8,max_length=10,description="Por favor preencha o campo CEP corretamente!")
    
class PhoneSchema(BaseModel):
    id:int
    ddd:int = Field(max_length=2,description="O campo DDD deve ter apenas 2 digitos.")
    number:int = Field(min_length=8,max_length=9, description="O campo de telefone deve ter até 9 digitos")

    @validator("ddd")
    def validator_ddd(cls,v):
        ddds = [11,12,13,14,15,16,17,18,19,21,22,24,27,28,31,32,33,34,35,37,38,41,42,43,44,45,46,
                47,48,49,51,53,54,55,61,62,63,64,65,66,67,68,69,71,73,74,75,77,79,81,82,83,84,85,86,87,88,89,91,
                92,93,94,95,96,97,98,99]
        if v not in ddds:
            raise ValueError("Este DDD não existe")
        return v
    



class CustomerSchema(BaseModel):
    id:int
    fantasy_name:str = Field(min_length=5,description="Por fvo preencha o nome fantasia corretamente")
    foundation:date = Field(default=date.today())
    sector:str = Field(min_length=6,description="O campo setor deve ser preenchido corretamente.") 
    service:str = Field(min_length=6,description="O campo setor deve ser preenchido corretamente.") 
    phone_id:int
    address_id:int

    @validator("sector")
    def sector_validation(cls, v):
        sectors = [
            "Agricultura, Pecuária e Pesca",
            "Alimentos e Bebidas",
            "Automotivo",
            "Aeroespacial e Defesa",
            "Atacado e Varejo",
            "Bancos e Serviços Financeiros",
            "Construção Civil",
            "Consultoria",
            "Educação",
            "Energia (Elétrica, Solar, etc.)",
            "Entretenimento e Mídia",
            "Farmacêutico e Biotecnologia",
            "Hotelaria e Turismo",
            "Imobiliário",
            "Indústria Química",
            "Logística e Transporte",
            "Manufatura",
            "Meio Ambiente",
            "Mineração",
            "Moda e Vestuário",
            "Papel e Celulose",
            "Petróleo e Gás",
            "Publicidade e Marketing",
            "Saúde e Bem-Estar",
            "Seguros",
            "Serviços Jurídicos",
            "Serviços Públicos",
            "Software e Tecnologia da Informação",
            "Telecomunicações",
            "Têxtil",
            "Terceirização de Serviços (BPO)",
            "Varejo Online (E-commerce)"
        ]   
        if v not in sectors:
            raise ValueError("O setor em questão não está na lista de stores permitidas.")
        return v
    
    @validator("service")
    def service_validator(cls,v):
        services = [
                "Consultoria Empresarial",
                "Consultoria Financeira",
                "Consultoria de TI",
                "Desenvolvimento de Software",
                "Hospedagem de Sites (Web Hosting)",
                "Design Gráfico",
                "Marketing Digital",
                "Publicidade e Propaganda",
                "Gestão de Redes Sociais",
                "Serviços Contábeis",
                "Serviços Jurídicos (Advocacia)",
                "Treinamento e Capacitação Profissional",
                "Tradução e Interpretação",
                "Serviços de Limpeza",
                "Serviços de Segurança Patrimonial",
                "Serviços de Vigilância Eletrônica",
                "Manutenção Predial",
                "Serviços de Manutenção e Reparo de Equipamentos",
                "Serviços de Entrega e Logística",
                "Serviços de Transporte (passageiros ou carga)",
                "Serviços de Saúde (clínicas, laboratórios, fisioterapia, etc.)",
                "Serviços de Estética e Beleza (salões, barbearias, etc.)",
                "Serviços de Alimentação (restaurantes, delivery, catering)",
                "Serviços Educacionais (escolas, cursos livres, EAD)",
                "Serviços Imobiliários (compra, venda, aluguel)",
                "Serviços de Engenharia e Arquitetura",
                "Serviços Ambientais (consultoria, coleta, reciclagem)",
                "Serviços de Recrutamento e Seleção (RH)",
                "Serviços Funerários",
                "Serviços de Produção de Eventos",
                "Serviços Fotográficos e Audiovisuais",
                "Serviços de Impressão e Cópias",
                "Serviços de TI (infraestrutura, suporte técnico, redes)"
            ]

        if v not in services:
            raise ValueError("O serviço em questão não está contido na lista de serviços permitidos")
        return v


class UserSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    mail_address:EmailStr = Field(min_length=20,description="O campo e-mail deve ser preenchido corretamente.") 
    phone_id:int
    customer_id:int
    address_id:int
    current_job:str =Field(min_length=8,description="O campo cargo atual deve ser preenchido corretamente.") 
    department:str = Field(min_length=8,description="O campo departamento deve ser preenchido corretamente.") 
    password:str = Field(min_length=8,max_length=20,description="Por favor preencha o campo senha corretamente.")

    @validator("department")
    def department_validator(cls, v):
        departments = ["Administrativo","Financeiro","Comercial","Recursos Humanos","Operacional","TI","Vendas"]
        if v not in departments:
            raise ValueError("O departamento inserido não existe!")
        return v



class ContractSchema(BaseModel):
    id:int
    tittle:str = Field(min_length=8,description="O campo titulo deve ser preenchido corretamente.") 
    date_sign:date
    objectives:str = Field(min_length=8,description="O campo objetivos deve ser preenchido corretamente.") 
    obligations:str = Field(min_length=8,description="O campo obligations deve ser preenchido corretamente.") 
    is_valid:bool
    archive:str
    customer_id:int

class ProjectSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    tech:str = Field(min_length=8,description="O campo tecnologias deve ser preenchido corretamente.") 
    methodology:str = Field(min_length=8,description="O campo metodologias deve ser preenchido corretamente.") 
    type:str = Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    date_start:date
    is_finished:bool
    customer_id:int
    contract_id:int



    @validator("methodology")
    def meth_validator(cls,v):
        meths = ["Waterfall","PMBOK","PRINCE2","SCRUM","KANBAN","LEAN","XP"]
        if v in meths:
            raise ValueError("A metodologia não é permitida a ser adicionada.")
        return v

    @validator("type")
    def type_validator(cls,v):
        types = [
            "Desenvolvimento de software",
            "Criação de aplicativo mobile",
            "Implantação de sistema ERP",
            "Automação de processos",
            "Criação de site institucional",
            "Construção de edifício",
            "Organização de evento",
            "Campanha publicitária",
            "Desenvolvimento de produto",
            "Redesign de marca",
            "Pesquisa de mercado",
            "Migração de dados",
            "Implantação de e-commerce",
            "Criação de curso online",
            "Elaboração de plano estratégico",
            "Lançamento de produto",
            "Implementação de BI (Business Intelligence)",
            "Abertura de nova filial",
            "Projeto de sustentabilidade",
            "Reestruturação organizacional"
        ]

        if v in types:
            raise ValueError("O tipo em questão não é permitido adicionar.")
        return type

class TaskSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    type:str =Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    date_created:date
    status:bool
    project_id:int
    customer_id:int


    

class JobSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    seniority:str =Field(min_length=8,description="O campo senioridade deve ser preenchido corretamente.") 
    budget:float 
    search_tool:str = Field(min_length=8,description="O campo ferramenta de busca deve ser preenchido corretamente.") 
    is_checked:bool 
    project_id:int
    customer_id:int

    @validator("schema_tool")
    def schema_tool_validator(cls,v):
        schemas = ["Linkedin Jobs","Zup","Interno","Social Media"]
        if v not in schemas:
            raise ValueError("A ferramenta em questão não é permitida ser adicionada")
        return v

class CandidateSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    mail_address:str = Field(min_length=8,description="O campo e-mail deve ser preenchido corretamente.") 
    phone_id:int
    approved:bool
    job_id:int

    

class SalesSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    type:str = Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    value:float
    date_register:date
    customer_id:int

    @validator("type")
    def type_validator(cls,v):
        types = []
        if v not in types:
            raise ValueError("O tipo em questão não é permitido ser adicionado.")
        return v

class FinancialSchema(BaseModel):
    id:int
    name:str = Field(min_length=8,description="O campo nome deve ser preenchido corretamente.") 
    type:str = Field(min_length=8,description="O campo tipo deve ser preenchido corretamente.") 
    value:float
    date_register:date
    is_recorrent:bool
    customer_id:int
    contract_id:int

    @validator("type")
    def type_validator(cls,v):
        types = ["Ativos","Passivo"]
        if v not in types:
            raise ValueError("O tipo em questão não é permitido ser adicionado.")
        return v







