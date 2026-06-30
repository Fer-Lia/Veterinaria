from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.mascota import MascotaCreate, MascotaUpdate, MascotaResponse
from app.services import mascota as servicio_mascota

router = APIRouter(prefix="/mascotas", tags=["Mascotas"])


@router.post("/", response_model=MascotaResponse, status_code=201)
def crear_mascota(mascota: MascotaCreate, db: Session = Depends(get_db)):
    try:
        return servicio_mascota.crear_mascota(db, mascota)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[MascotaResponse])
def listar_mascotas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return servicio_mascota.obtener_mascotas(db, skip, limit)


@router.get("/{mascota_id}", response_model=MascotaResponse)
def obtener_mascota(mascota_id: int, db: Session = Depends(get_db)):
    mascota = servicio_mascota.obtener_mascota_por_id(db, mascota_id)
    if mascota is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@router.put("/{mascota_id}", response_model=MascotaResponse)
def actualizar_mascota(mascota_id: int, mascota: MascotaUpdate, db: Session = Depends(get_db)):
    mascota_actualizada = servicio_mascota.actualizar_mascota(db, mascota_id, mascota)
    if mascota_actualizada is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota_actualizada


@router.delete("/{mascota_id}", status_code=204)
def eliminar_mascota(mascota_id: int, db: Session = Depends(get_db)):
    eliminado = servicio_mascota.eliminar_mascota(db, mascota_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")