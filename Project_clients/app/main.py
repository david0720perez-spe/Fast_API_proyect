from fastapi import FastAPI
from app.enrutador import clientes, facturas

# Crear la instancia de FastAPI
app = FastAPI()

# Incluir los routers
app.include_router(clientes.router)
app.include_router(facturas.router)

# Ruta raíz
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a mi API de clientes y facturas"}