from pydantic import BaseModel

class Client(BaseModel):
    id_: int
    name: str
    email: str
    telefone: str

class ClientCreateUpdate(BaseModel):
    name: str
    email: str
    telefone: str