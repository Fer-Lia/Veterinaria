from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.cliente import ClienteCreate, ClienteUpdate, ClienteResponse
from app.services import cliente as servicio_cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/", response_model=ClienteResponse, status_code=201)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    try:
        return servicio_cliente.crear_cliente(db, cliente)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return servicio_cliente.obtener_clientes(db, skip, limit)


@router.get("/{cliente_id}", response_model=ClienteResponse)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = servicio_cliente.obtener_cliente_por_id(db, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente


@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    cliente_actualizado = servicio_cliente.actualizar_cliente(db, cliente_id, cliente)
    if cliente_actualizado is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_actualizado


@router.delete("/{cliente_id}", status_code=204)
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    eliminado = servicio_cliente.eliminar_cliente(db, cliente_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")