from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.veterinario import Veterinario
from app.schemas.veterinario import VeterinarioCreate, VeterinarioUpdate


def crear_veterinario(db: Session, veterinario: VeterinarioCreate) -> Veterinario:
    nuevo_veterinario = Veterinario(**veterinario.model_dump())
    db.add(nuevo_veterinario)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Ya existe un veterinario con ese DNI")
    db.refresh(nuevo_veterinario)
    return nuevo_veterinario


def obtener_veterinarios(db: Session, skip: int = 0, limit: int = 100) -> list[Veterinario]:
    return db.query(Veterinario).offset(skip).limit(limit).all()


def obtener_veterinario_por_id(db: Session, veterinario_id: int) -> Veterinario | None:
    return db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()


def actualizar_veterinario(db: Session, veterinario_id: int, veterinario: VeterinarioUpdate) -> Veterinario | None:
    veterinario_existente = obtener_veterinario_por_id(db, veterinario_id)
    if veterinario_existente is None:
        return None

    datos_actualizados = veterinario.model_dump(exclude_unset=True)
    for campo, valor in datos_actualizados.items():
        setattr(veterinario_existente, campo, valor)

    db.commit()
    db.refresh(veterinario_existente)
    return veterinario_existente


def eliminar_veterinario(db: Session, veterinario_id: int) -> bool:
    veterinario_existente = obtener_veterinario_por_id(db, veterinario_id)
    if veterinario_existente is None:
        return False

    db.delete(veterinario_existente)
    db.commit()
    return True