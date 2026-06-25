from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class ClienteBase(BaseModel):
    dni: str
    nombre: str
    apellido: str
    direccion: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    direccion: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None


class ClienteResponse(ClienteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fecha_registro: datetime