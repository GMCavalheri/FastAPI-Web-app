from fastapi import APIRouter

from app.models.client import Client

router = APIRouter(
    prefix="/clients"
)

CLIENTS_LIST = [Client(id_ = 1, name="Bob Good", email="bob@good.com", telefone="993949596"),
                    Client(id_ = 2, name="Michael Bad", email="mic@bad.com", telefone="966666666")]

@router.get("/", response_model=list[Client])
async def list_clients():
    return CLIENTS_LIST

@router.get("/{client_id}", response_model=Client | None)
async def obtain_client(client_id: int):
    for client in CLIENTS_LIST:
        if client.id_ == client_id:
            return client
    return None