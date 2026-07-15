from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.routes import client

templates = Jinja2Templates(directory="templates")

app = FastAPI(
   title="Techlog Solutions API",
   description="CRM for Techlog Solutions",
   version="1.0.0", 
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(client.router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
async def front_page(request: Request):
   return templates.TemplateResponse("index.html", {"request":request, "title": "Techlog Solutions CRM", "version": "1.0.0"})