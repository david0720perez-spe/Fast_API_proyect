from fastapi import FastAPI
from datetime import datetime
from Model.cliente import (
    Cliente,
    ClienteBase,
    ClienteCrear,
    ClienteEditar,
    ClienteEliminar
)

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a mi API de clientes"}

# Lista temporal
lista_clientes: list[Cliente] = []


# LISTAR CLIENTES
@app.get("/clientes")
async def listar_clientes():
    return {"clientes": lista_clientes}


# CREAR CLIENTE
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):

    cliente_val_id = len(lista_clientes) + 1

    # Crear cliente con ID
    cliente_val = Cliente(
        id=cliente_val_id,
        **datos_cliente.model_dump()
    )

    lista_clientes.append(cliente_val)

    return cliente_val


# OBTENER UN CLIENTE
@app.get("/clientes/{id}")
async def obtener_cliente(id: int):

    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente

    return {"mensaje": "Cliente no encontrado"}


# EDITAR CLIENTE
@app.put("/clientes/{id}")
async def editar_cliente(id: int, datos_cliente: ClienteEditar):

    for i, obj_cliente in enumerate(lista_clientes):

        if obj_cliente.id == id:

            cliente_actualizado = Cliente(
                id=id,
                **datos_cliente.model_dump()
            )

            # Reemplazar cliente en la lista
            lista_clientes[i] = cliente_actualizado

            return {
                "mensaje": "Cliente actualizado correctamente",
                "cliente": cliente_actualizado
            }

    return {"mensaje": "Cliente no encontrado"}


# ELIMINAR CLIENTE
@app.delete("/clientes/{id}")
async def eliminar_cliente(id: int):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            lista_clientes.pop(i)

            return {
                "mensaje": f"Cliente {id} eliminado"
            }

    return {"mensaje": "Cliente no encontrado"}