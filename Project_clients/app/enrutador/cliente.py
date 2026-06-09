from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Cliente, ClienteCrear, ClienteEditar

router = APIRouter(prefix="/clientes", tags=["clientes"])

lista_clientes: list[Cliente] = []

@router.get("/", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

@router.post("/", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_id = len(lista_clientes) + 1
    cliente = Cliente(id=cliente_id, **datos_cliente.model_dump())
    lista_clientes.append(cliente)
    return cliente

