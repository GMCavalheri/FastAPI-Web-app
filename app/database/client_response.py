from app.database.local import LocalDatabase
from app.models.client import Client

class ClientRepository:
    def __init__(self, database: LocalDatabase):
        self.db = database

    async def list_clients(self) -> list[Client]:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, email, telefone FROM clients")
            lines = cursor.fetchall()
            clients = [
                Client(id_= line[0], name=line[1], email=line[2], telefone=line[3])
                for line in lines
            ]
            return clients
    
    async def obtain_client(self, client_id: int) -> Client | None:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, email, telefone FROM clients WHERE id = ?", (client_id,))
            line = cursor.fetchall()
            if line:
                return Client(id_= line[0], name=line[1], email=line[2], telefone=line[3])
            return None