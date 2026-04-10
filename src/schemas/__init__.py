from src.schemas.base import AuditFields, RequestBase, ResponseBase, ListaResponse
from src.schemas.usuario import (
    UsuarioRequest,
    UsuarioUpdateRequest,
    UsuarioResponse,
    UsuarioDeleteResponse,
)
from src.schemas.animal import (
    AnimalRequest,
    AnimalUpdateRequest,
    AnimalResponse,
    GatoRequest,
    GatoUpdateRequest,
    GatoResponse,
    PerroRequest,
    PerroUpdateRequest,
    PerroResponse,
    AnimalDeleteResponse,
)
from src.schemas.cita import (
    CitaRequest,
    CitaUpdateRequest,
    CitaResponse,
    CitaDeleteResponse,
)
from src.schemas.consulta import (
    ConsultaRequest,
    ConsultaUpdateRequest,
    ConsultaResponse,
    ConsultaDeleteResponse,
)

__all__ = [
    "AuditFields",
    "RequestBase",
    "ResponseBase",
    "ListaResponse",
    "UsuarioRequest",
    "UsuarioUpdateRequest",
    "UsuarioResponse",
    "UsuarioDeleteResponse",
    "AnimalRequest",
    "AnimalUpdateRequest",
    "AnimalResponse",
    "GatoRequest",
    "GatoUpdateRequest",
    "GatoResponse",
    "PerroRequest",
    "PerroUpdateRequest",
    "PerroResponse",
    "AnimalDeleteResponse",
    "CitaRequest",
    "CitaUpdateRequest",
    "CitaResponse",
    "CitaDeleteResponse",
    "ConsultaRequest",
    "ConsultaUpdateRequest",
    "ConsultaResponse",
    "ConsultaDeleteResponse",
]
