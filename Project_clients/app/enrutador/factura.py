from fastapi import APIRouter, HTTPException
from ..modelos.factura import Factura, FacturaCrear, FacturaEditar

router = APIRouter(prefix="/facturas", tags=["facturas"])

# Lista temporal para almacenar facturas (en memoria)
lista_facturas: list[Factura] = []

# LISTAR TODAS LAS FACTURAS
@router.get("/", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

# CREAR UNA FACTURA
@router.post("/", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear):
    # Lógica robusta para generar ID: 
    # El nuevo ID será el mayor existente + 1, o 1 si la lista está vacía
    nuevo_id = 1
    if lista_facturas:
        nuevo_id = max(factura.id for factura in lista_facturas) + 1
    
    factura = Factura(id=nuevo_id, **datos_factura.model_dump())
    lista_facturas.append(factura)
    return factura

# OBTENER UNA FACTURA POR ID
@router.get("/{id}", response_model=Factura)
async def obtener_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            return factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")

# EDITAR UNA FACTURA
@router.put("/{id}", response_model=Factura)
async def editar_factura(id: int, datos_factura: FacturaEditar):
    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            # Creamos la nueva instancia conservando el ID original
            factura_actualizada = Factura(id=id, **datos_factura.model_dump())
            lista_facturas[i] = factura_actualizada
            return factura_actualizada
    raise HTTPException(status_code=404, detail="Factura no encontrada")

# ELIMINAR UNA FACTURA
@router.delete("/{id}")
async def eliminar_factura(id: int):
    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas.pop(i)
            return {"mensaje": f"Factura {id} eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Factura no encontrada")