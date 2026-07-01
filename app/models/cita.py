from sqlalchemy import Column, Integer, String, DateTime, Time, Enum, ForeignKey
import enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base

class EstadoCita(enum.Enum):
    programada = "programada"
    completada = "completada"

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, unique=True, primary_key=True, index=True, autoincrement=True)
    fecha = Column(DateTime(timezone=True), nullable=False)
    hora = Column(Time, nullable=False)
    motivo = Column(String(200), nullable=False)
    estado = Column(Enum(EstadoCita), nullable=False, default=EstadoCita.programada)

    id_mascota = Column(Integer, ForeignKey("mascotas.id_mascota"), nullable=True)
    dni_veterinario = Column(String(15), ForeignKey("veterinarios.dni"), nullable=True)

    mascota = relationship("Mascota", back_populates="citas")
    veterinario = relationship("Veterinario", back_populates="citas")




