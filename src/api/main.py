"""
Aplicación principal FastAPI.

Contiene la instancia de la app y configuración de middlewares.
Los endpoints están organizados en routers separados.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import (
    usuario_router,
    animal_router,
    cita_router,
    consulta_router,
)

app = FastAPI(
    title="API Veterinaria",
    description="API REST para el sistema de gestión de veterinaria",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_router)
app.include_router(animal_router)
app.include_router(cita_router)
app.include_router(consulta_router)


@app.get("/health", tags=["health"])
async def health_check():
    """Endpoint de verificación de estado de la API.

    Returns:
        Estado del servicio.
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
