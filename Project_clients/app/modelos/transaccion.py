from pydantic import BaseModel
from .cliente import Cliente
from .factura import Factura

class TransaccionBase(BaseModel):
    cliente: Cliente
    factura: Factura
    metodo_pago: str  
    estado: str       

class TransaccionCrear(BaseModel):
    cliente_id: int
    factura_id: int
    metodo_pago: str
    estado: str | None = "Pendiente"

class Transaccion(TransaccionBase):
    id: int

class TransaccionEditar(BaseModel):
    metodo_pago: str | None = None
    estado: str | None = None