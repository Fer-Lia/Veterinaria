from datetime import datetime, time
from pydantic import BaseModel, ConfigDict
from enum import Enum

class EstadoCita(str, Enum):
    programada = "programada"
    completada = "completada"

class CitaBase(BaseModel):
    dni_veterinario: str
    id_mascota: int
    fecha: datetime
    hora: time | None
    motivo: str
    estado: EstadoCita

class CitaCreate(CitaBase):
    pass

class CitaUpdate(BaseModel):
    fecha: datetime | None = None
    hora: time | None = None
    motivo: str | None = None
    estado: EstadoCita | None = None
    id_mascota: int | None = None
    dni_veterinario: str | None = None


class CitaResponse(CitaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int