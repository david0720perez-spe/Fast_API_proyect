from pydantic import BaseModel
class Factura(BaseModel):
    id:int
    fecha:str
    total:float
    cliente:str
    trasaccion:list[str]
    