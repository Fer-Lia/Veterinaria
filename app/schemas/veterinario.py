from pydantic import BaseModel, ConfigDict


class VeterinarioBase(BaseModel):
    dni: str
    nombre: str
    apellido: str
    especialidad: str | None = None
    telefono: str | None = None


class VeterinarioCreate(VeterinarioBase):
    pass


class VeterinarioUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    especialidad: str | None = None
    telefono: str | None = None


class VeterinarioResponse(VeterinarioBase):
    model_config = ConfigDict(from_attributes=True)

    id: int