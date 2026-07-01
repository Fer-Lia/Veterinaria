from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.cita import Cita
from app.schemas.cita import CitaCreate, CitaUpdate

def crear_cita(db: Session, cita: CitaCreate) -> Cita:
    nueva_cita = Cita(**cita.model_dump())
    db.add(nueva_cita)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("No se pudo crear la cita")
    db.refresh(nueva_cita)
    return nueva_cita


def obtener_citas(db: Session, skip: int = 0, limit: int = 100) -> list[Cita]:
    return db.query(Cita).offset(skip).limit(limit).all()


def obtener_cita_por_id(db: Session, id: int) -> Cita | None:
    return db.query(Cita).filter(Cita.id == id).first()


def actualizar_cita(db: Session, id: int, cita: CitaUpdate) -> Cita | None:
    cita_existente = obtener_cita_por_id(db, id)
    if cita_existente is None:
        return None

    datos_actualizados = cita.model_dump(exclude_unset=True)
    for campo, valor in datos_actualizados.items():
        setattr(cita_existente, campo, valor)

    db.commit()
    db.refresh(cita_existente)
    return cita_existente


def eliminar_cita(db: Session, id: int) -> bool:
    cita_existente = obtener_cita_por_id(db, id)
    if cita_existente is None:
        return False

    db.delete(cita_existente)
    db.commit()
    return True