from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.models.client import Client
from app.database.client_response import ClientRepository
from app.dependences import obtain_repository_client

router = APIRouter(
    prefix="/clients"
)

CLIENTS_LIST = [Client(id_ = 1, name="Bob Good", email="bob@good.com", telefone="993949596"),
                    Client(id_ = 2, name="Michael Bad", email="mic@bad.com", telefone="966666666")]

@router.get("/", response_model=list[Client])
async def list_clients(client_repository: Annotated[ClientRepository, Depends(obtain_repository_client)]):
    return await client_repository.list_clients()

@router.get("/{client_id}", response_model=Client | None)
async def obtain_client(client_repository: Annotated[ClientRepository, Depends(obtain_repository_client)],
    client_id: int):

    client = await client_repository.obtain_client(client_id)

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    return client