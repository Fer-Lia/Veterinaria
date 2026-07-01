from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.cita import CitaCreate, CitaUpdate, CitaResponse
from app.services import cita as servicio_cita

router = APIRouter(prefix="/citas", tags=["Citas"])


@router.post("/", response_model=CitaResponse, status_code=201)
def crear_cita(cita: CitaCreate, db: Session = Depends(get_db)):
    try:
        return servicio_cita.crear_cita(db, cita)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[CitaResponse])
def listar_citas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return servicio_cita.obtener_citas(db, skip, limit)

@router.get("/{id}", response_model=CitaResponse)
def obtener_cita(id: int, db: Session = Depends(get_db)):
    cita = servicio_cita.obtener_cita_por_id(db, id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.put("/{id}", response_model=CitaResponse)
def actualizar_cita(id: int, cita: CitaUpdate, db: Session = Depends(get_db)):
    cita_actualizada = servicio_cita.actualizar_cita(db, id, cita)
    if cita_actualizada is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita_actualizada


@router.delete("/{id}", status_code=204)
def eliminar_cita(id: int, db: Session = Depends(get_db)):
    eliminado = servicio_cita.eliminar_cita(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cita no encontrada")