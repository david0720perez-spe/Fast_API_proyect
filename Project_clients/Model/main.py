# archivo main.py
from fastapi import FastAPI

# 1. Importaciones limpias desde cliente.py (sin el punto)
from cliente import (
    Cliente,
    ClienteBase,
    ClienteCrear,
    ClienteEditar,  # Agregado para que no falle el PUT de clientes
)

# 2. Importaciones corregidas desde factura.py
from factura import (
    Factura,
    FacturaCrear,
    FacturaEditar,
)

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a mi API de clientes y facturas"}

# Listas temporales en memoria
lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []  # Lista temporal para las facturas



@app.get("/clientes")
async def listar_clientes():
    return {"clientes": lista_clientes}

@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val_id = len(lista_clientes) + 1
    cliente_val = Cliente(
        id=cliente_val_id,
        **datos_cliente.model_dump()
    )
    lista_clientes.append(cliente_val)
    return cliente_val

@app.get("/clientes/{id}")
async def obtener_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    return {"mensaje": "Cliente no encontrado"}

@app.put("/clientes/{id}")
async def editar_cliente(id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_actualizado = Cliente(
                id=id,
                **datos_cliente.model_dump()
            )
            lista_clientes[i] = cliente_actualizado
            return {
                "mensaje": "Cliente actualizado correctamente",
                "cliente": cliente_actualizado
            }
    return {"mensaje": "Cliente no encontrado"}

@app.delete("/clientes/{id}")
async def eliminar_cliente(id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes.pop(i)
            return {"mensaje": f"Cliente {id} eliminado"}
    return {"mensaje": "Cliente no encontrado"}



# LISTAR FACTURAS
@app.get("/facturas")
async def listar_facturas():
    return {"facturas": lista_facturas}

# CREAR FACTURA
@app.post("/facturas", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear):
    factura_val_id = len(lista_facturas) + 1  # Auto-incremental temporal
    factura_val = Factura(
        id=factura_val_id,
        **datos_factura.model_dump()
    )
    lista_facturas.append(factura_val)
    return factura_val

# OBTENER UNA FACTURA
@app.get("/facturas/{id}")
async def obtener_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            return factura
    return {"mensaje": "Factura no encontrada"}

# EDITAR FACTURA
@app.put("/facturas/{id}")
async def editar_factura(id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id:
            factura_actualizada = Factura(
                id=id,
                **datos_factura.model_dump()
            )
            lista_facturas[i] = factura_actualizada
            return {
                "mensaje": "Factura actualizada correctamente",
                "factura": factura_actualizada
            }
    return {"mensaje": "Factura no encontrada"}

# ELIMINAR FACTURA
@app.delete("/facturas/{id}")
async def eliminar_factura(id: int):
    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas.pop(i)
            return {"mensaje": f"Factura {id} eliminada correctamente"}
    return {"mensaje": "Factura no encontrada"}