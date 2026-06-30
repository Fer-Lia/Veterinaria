from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.veterinario import VeterinarioCreate, VeterinarioUpdate, VeterinarioResponse
from app.services import veterinario as servicio_veterinario

router = APIRouter(prefix="/veterinarios", tags=["Veterinarios"])


@router.post("/", response_model=VeterinarioResponse, status_code=201)
def crear_veterinario(veterinario: VeterinarioCreate, db: Session = Depends(get_db)):
    try:
        return servicio_veterinario.crear_veterinario(db, veterinario)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[VeterinarioResponse])
def listar_veterinarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return servicio_veterinario.obtener_veterinarios(db, skip, limit)


@router.get("/{veterinario_id}", response_model=VeterinarioResponse)
def obtener_veterinario(veterinario_id: int, db: Session = Depends(get_db)):
    veterinario = servicio_veterinario.obtener_veterinario_por_id(db, veterinario_id)
    if veterinario is None:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")
    return veterinario


@router.put("/{veterinario_id}", response_model=VeterinarioResponse)
def actualizar_veterinario(veterinario_id: int, veterinario: VeterinarioUpdate, db: Session = Depends(get_db)):
    veterinario_actualizado = servicio_veterinario.actualizar_veterinario(db, veterinario_id, veterinario)
    if veterinario_actualizado is None:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")
    return veterinario_actualizado


@router.delete("/{veterinario_id}", status_code=204)
def eliminar_veterinario(veterinario_id: int, db: Session = Depends(get_db)):
    eliminado = servicio_veterinario.eliminar_veterinario(db, veterinario_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")