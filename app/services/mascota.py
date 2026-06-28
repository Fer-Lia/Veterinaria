from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.mascota import Mascota
from app.schemas.mascota import MascotaCreate, MascotaUpdate


def crear_mascota(db: Session, mascota: MascotaCreate) -> Mascota:
    nueva_mascota = Mascota(**mascota.model_dump())
    db.add(nueva_mascota)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("El DNI del cliente no existe en la tabla de clientes")
    db.refresh(nueva_mascota)
    return nueva_mascota


def obtener_mascotas(db: Session, skip: int = 0, limit: int = 100) -> list[Mascota]:
    return db.query(Mascota).offset(skip).limit(limit).all()


def obtener_mascota_por_id(db: Session, mascota_id: int) -> Mascota | None:
    return db.query(Mascota).filter(Mascota.id_mascota == mascota_id).first()


def actualizar_mascota(db: Session, mascota_id: int, mascota: MascotaUpdate) -> Mascota | None:
    mascota_existente = obtener_mascota_por_id(db, mascota_id)
    if mascota_existente is None:
        return None

    datos_actualizados = mascota.model_dump(exclude_unset=True)
    for campo, valor in datos_actualizados.items():
        setattr(mascota_existente, campo, valor)

    db.commit()
    db.refresh(mascota_existente)
    return mascota_existente


def eliminar_mascota(db: Session, mascota_id: int) -> bool:
    mascota_existente = obtener_mascota_por_id(db, mascota_id)
    if mascota_existente is None:
        return False

    db.delete(mascota_existente)
    db.commit()
    return True