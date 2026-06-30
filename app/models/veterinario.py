from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dni = Column(String(20), primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=True)
    telefono = Column(String(20), nullable=True)