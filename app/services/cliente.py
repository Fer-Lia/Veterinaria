from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate


def crear_cliente(db: Session, cliente: ClienteCreate) -> Cliente:
    nuevo_cliente = Cliente(**cliente.model_dump())
    db.add(nuevo_cliente)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Ya existe un cliente con ese DNI o email")
    db.refresh(nuevo_cliente)
    return nuevo_cliente


def obtener_clientes(db: Session, skip: int = 0, limit: int = 100) -> list[Cliente]:
    return db.query(Cliente).offset(skip).limit(limit).all()


def obtener_cliente_por_id(db: Session, cliente_id: int) -> Cliente | None:
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()


def actualizar_cliente(db: Session, cliente_id: int, cliente: ClienteUpdate) -> Cliente | None:
    cliente_existente = obtener_cliente_por_id(db, cliente_id)
    if cliente_existente is None:
        return None

    datos_actualizados = cliente.model_dump(exclude_unset=True)
    for campo, valor in datos_actualizados.items():
        setattr(cliente_existente, campo, valor)

    db.commit()
    db.refresh(cliente_existente)
    return cliente_existente


def eliminar_cliente(db: Session, cliente_id: int) -> bool:
    cliente_existente = obtener_cliente_por_id(db, cliente_id)
    if cliente_existente is None:
        return False

    db.delete(cliente_existente)
    db.commit()
    return True