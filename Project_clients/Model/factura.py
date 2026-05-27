# archivo: Model/factura.py
from pydantic import BaseModel
from datetime import datetime

class FacturaBase(BaseModel):
    fecha: str
    total: float
    cliente: str
    transaccion: list[str]  

class FacturaCrear(FacturaBase):
    pass  

class FacturaEditar(FacturaBase):
    pass  

class Factura(FacturaBase):
    id: int  
