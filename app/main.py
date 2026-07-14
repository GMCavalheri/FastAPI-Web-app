from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.routes import client

app = FastAPI(
   title="Techlog Solutions API",
   description="CRM for Techlog Solutions",
   version="1.0.0", 
)

app.include_router(client.router)


@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/front", response_class=HTMLResponse)
async def front_page():
   html_content = """
   <html>
        <head>
            <title>Techlog Solutions</title>
        </head>
        <body>
            <h1>Techlog Solutions</h1>
            <p>Service Order Management System</p>
            <p>Status: <strong>Operational</strong></p>
        </body>
   </html>
   """
   return html_content