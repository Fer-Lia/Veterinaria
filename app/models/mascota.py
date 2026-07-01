from datetime import date

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Mascota(Base):
    __tablename__ = "mascotas"

    id_mascota = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)
    raza = Column(String(100), nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    dni_cliente = Column(String(15), ForeignKey("clientes.dni"), nullable=False)

    cliente = relationship("Cliente", back_populates="mascotas")
    citas = relationship("Cita", back_populates="mascota")
