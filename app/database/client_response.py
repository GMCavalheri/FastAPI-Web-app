from app.database.local import LocalDatabase
from app.models.client import Client, ClientCreateUpdate


class ClientRepository:
    def __init__(self, database: LocalDatabase):
        self.db = database

    async def list_clients(self) -> list[Client]:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT id, name, email, telefone FROM clients")
            
            lines = cursor.fetchall()
            
            clients = [
                Client(id_=line[0], name=line[1], email=line[2], telefone=line[3])
                for line in lines
            ]

            return clients
    
    async def obtain_client(self, client_id: int) -> Client | None:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT id, name, email, telefone FROM clients WHERE id = ?",
                            (client_id,))
            
            line = cursor.fetchall()
            
            if line:
                return Client(id_= line[0], name=line[1], email=line[2], telefone=line[3])
            
            return None
        
    async def create_client(self, client: ClientCreateUpdate) -> Client:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            
            cursor.execute("INSERT INTO clients (name, email, telefone) VALUES (?, ?, ?)",
                            (client.name, client.email, client.telefone))
            
            client_id = cursor.lastrowid
            
            return Client(id_=client_id, name=client.name, email=client.email, telefone=client.telefone)
        
    
    async def update_client(self, client_id: int, client: ClientCreateUpdate) -> Client | None:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE clients SET name = ?, email = ?, telefone = ? WHERE id = ?",
                            (client.name, client.email, client.telefone, client_id))
            
            if cursor.rowcount == 0:
                return None

            return Client(id_=client_id, name=client.name, email=client.email, telefone=client.telefone)
        
    async def delete_client(self, client_id: int) -> bool:
        with self.db.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?",
                            (client_id,))

            return cursor.rowcount > 0         
        