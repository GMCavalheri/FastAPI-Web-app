from typing import Annotated
from fastapi import Depends

from app.database.local import LocalDatabase
from app.database.client_response import ClientRepository

database = LocalDatabase()

def obtain_database() -> LocalDatabase:
    return database

def obtain_repository_client(
        local_database: Annotated[LocalDatabase, 
                                  Depends(obtain_database)]
                             ) -> ClientRepository:
    return ClientRepository(local_database)