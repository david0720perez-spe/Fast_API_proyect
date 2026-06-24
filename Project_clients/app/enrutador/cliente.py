from fastapi import APIRouter, HTTPException, status
from app.modelos.cliente import Cliente, ClienteCrear, ClienteEditar

router = APIRouter(prefix="/clientes", tags=["clientes"])

lista_clientes: list[Cliente] = []

@router.get("/", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes

# Opcional: Obtener un solo cliente por ID (muy útil para el frontend)
@router.get("/{cliente_id}", response_model=Cliente)
async def obtener_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Cliente no encontrado"
    )

@router.post("/", response_model=Cliente, status_code=status.HTTP_201_CREATED)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_id = len(lista_clientes) + 1
    cliente = Cliente(id=cliente_id, **datos_cliente.model_dump())
    lista_clientes.append(cliente)
    return cliente

@router.put("/{cliente_id}", response_model=Cliente)
async def actualizar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            # Creamos el objeto actualizado manteniendo el mismo ID
            cliente_actualizado = Cliente(id=cliente_id, **datos_cliente.model_dump())
            lista_clientes[i] = cliente_actualizado
            return cliente_actualizado
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Cliente no encontrado"
    )

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == cliente_id:
            lista_clientes.pop(i)
            return  # Al usar 204 No Content, no se devuelve cuerpo en la respuesta
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Cliente no encontrado"
    )
