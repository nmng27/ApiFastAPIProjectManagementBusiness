from models.All.models import Address, Phone
from Schemas.Schema import Address as AddressSchema, PhoneSchema
from services.services import AddressService, PhoneService
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/address",response_model=Add)
def create_address(addres:Address):
    try:
        AddressService.create(addres)
        
    except HTTPException as ex:
        raise ex


@app.put("/address/{id}")
def update_user(new_address:Address,id:int):
    try:
        AddressService.update(id,new_address)

        
    except HTTPException as ex:
        raise ex
    
@app.post("/phone")
def create(phone:Phone):
    try:
        PhoneService.create(phone)
    except HTTPException as ex:
        raise ex
    
@app.put("/phne/{id}")
def update(id:int, phone:Phone):
    try:
        PhoneService.update(id,phone)
    except  HTTPException as ex:
        raise ex

