from fastapi import FastAPI
from app.enrutador import cliente, factura, transaccion

# Crear la instancia de FastAPI
app = FastAPI()

# Incluir los routers
app.include_router(cliente.router)
app.include_router(factura.router)
app.include_router(transaccion.router)
# Ruta raíz
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a mi API de clientes y facturas"}