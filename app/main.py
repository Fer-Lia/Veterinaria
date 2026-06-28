from fastapi import FastAPI

from app.db.database import Base, engine
from app.routers import cliente, mascota


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Veterinaria")

app.include_router(cliente.router)
app.include_router(mascota.router)

@app.get("/health-db")
def health_check():
    return {"status": "ok", "mensaje": "Conexión a la base de datos funcionando"}