from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.models.client import Client, ClientCreateUpdate
from app.database.client_response import ClientRepository
from app.dependences import obtain_repository_client

router = APIRouter(
    prefix="/clients"
)


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


@router.post("/", response_model=Client, status_code=201)
async def create_client(
                        client_repository: Annotated[ClientRepository, Depends(obtain_repository_client)],
                        client: ClientCreateUpdate
    ):
    
    return await client_repository.create_client(client)


@router.put("/{client_id}", response_model=Client | None)
async def update_client(
    client_repository: Annotated[ClientRepository, Depends(obtain_repository_client)], 
    client_id: int,
    client: ClientCreateUpdate):

    update_client = await client_repository.update_client(client_id, client)

    if not update_client:
        raise HTTPException(status_code=404, detail="Client not found!")

    return update_client


@router.delete("/{client_id}", status_code=204)
async def delete_client(
    client_repository: Annotated[ClientRepository, Depends(obtain_repository_client)],
    client_id: int):

    success = await client_repository.delete_client(client_id)
    if not success:
        raise HTTPException(status_code=404, detail="Client not found")
    
