from fastapi import FastAPI

app = FastAPI()

from app.enrutador import clientes

app.include_router(clientes.router)