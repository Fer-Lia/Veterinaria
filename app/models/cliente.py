from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String(15), unique=True, nullable=False, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    direccion = Column(String(300), nullable=True)
    telefono = Column(String(15), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    telefono_secundario = Column(String(15), nullable=True)

    mascotas = relationship("Mascota", back_populates="cliente")



