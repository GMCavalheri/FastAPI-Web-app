from fastapi import APIRouter

from app.models.client import Client

router = APIRouter(
    prefix="/clients"
)

@router.get("/", response_model=list[Client])
async def list_clients():
    
    clients_list = [Client(name="Bob Good", email="bob@good.com", telefone="993949596"),
                    Client(name="Michael Bad", email="mic@bad.com", telefone="966666666")]
    
    return clients_list