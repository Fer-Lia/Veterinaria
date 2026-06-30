from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class MascotaBase(BaseModel):
    nombre: str
    especie: str
    raza: str | None = None
    fecha_nacimiento: date | None = None
    dni_cliente: str


class MascotaCreate(MascotaBase):
    pass


class MascotaUpdate(BaseModel):
    nombre: str | None = None
    especie: str | None = None
    raza: str | None = None
    fecha_nacimiento: date | None = None


class MascotaResponse(MascotaBase):
    model_config = ConfigDict(from_attributes=True)

    id_mascota: int