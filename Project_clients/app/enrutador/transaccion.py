from fastapi import APIRouter, HTTPException
from ..modelos.transaccion import Transaccion, TransaccionCrear, TransaccionEditar
from .cliente import lista_clientes
from .factura import lista_facturas

router = APIRouter(prefix="/transacciones", tags=["transacciones"])

lista_transacciones: list[Transaccion] = []

# 1. CREAR TRANSACCIÓN (Basada en Cliente y Factura)
@router.post("/", response_model=Transaccion)
async def crear_transaccion(datos: TransaccionCrear):
    # Buscar el cliente en la lista de clientes
    cliente_encontrado = None
    for c in lista_clientes:
        if c.id == datos.cliente_id:
            cliente_encontrado = c
            break
            
    # Buscar la factura en la lista de facturas
    factura_encontrada = None
    for f in lista_facturas:
        if f.id == datos.factura_id:
            factura_encontrada = f
            break

    # Validar que ambos existan antes de proceder
    if not cliente_encontrado:
        raise HTTPException(status_code=404, detail="El Cliente especificado no existe")
    if not factura_encontrada:
        raise HTTPException(status_code=404, detail="La Factura especificada no existe")

    # Si ambos existen, creamos la transacción uniendo los datos
    transaccion_id = len(lista_transacciones) + 1
    nueva_transaccion = Transaccion(
        id=transaccion_id,
        cliente=cliente_encontrado,  # Inyectamos el objeto Cliente completo
        factura=factura_encontrada,  # Inyectamos el objeto Factura completo
        metodo_pago=datos.metodo_pago,
        estado=datos.estado
    )
    
    lista_transacciones.append(nueva_transaccion)
    return nueva_transaccion

# 2. LISTAR TODAS LAS TRANSACCIONES
@router.get("/", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

# 3. OBTENER UNA TRANSACCIÓN POR ID
@router.get("/{id}", response_model=Transaccion)
async def obtener_transaccion(id: int):
    for t in lista_transacciones:
        if t.id == id:
            return t
    raise HTTPException(status_code=404, detail="Transacción no encontrada")