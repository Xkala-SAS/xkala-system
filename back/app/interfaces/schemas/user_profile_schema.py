from pydantic import BaseModel

from typing import List, Optional

from datetime import datetime


# =========================
# DOCUMENTO
# =========================

class DocumentResponse(BaseModel):

    tipo: str

    numero: str


# =========================
# DIRECCIÓN
# =========================

class AddressResponse(BaseModel):

    direccion: str

    barrio: str

    ciudad: str

    departamento: str


# =========================
# CONTACTOS
# =========================

class ContactResponse(BaseModel):

    tipo: str

    valor: str

    principal: bool


# =========================
# AFILIACIONES
# =========================

class AffiliationsResponse(BaseModel):

    eps: str

    arl: str

    pension: str

    cesantias: str


# =========================
# LABORAL
# =========================

class LaboralResponse(BaseModel):

    cargo: str

    tipo_contrato: str

    fecha_ingreso: datetime

    remuneration_type: str

    remuneration_value: float

    activo: bool


# =========================
# TALLAS
# =========================

class SizesResponse(BaseModel):

    camisa: str

    pantalon: str

    zapato: str


# =========================
# ARCHIVOS
# =========================

class FileResponse(BaseModel):

    tipo: str

    ruta: str


# =========================
# PERFIL COMPLETO
# =========================

class UserProfileResponse(BaseModel):

    id: str

    nombre_completo: str

    email: str

    estado: bool

    rol: str

    permissions: List[str] = []

    documento: Optional[DocumentResponse] = None

    direccion: Optional[AddressResponse] = None

    contactos: List[ContactResponse] = []

    afiliaciones: Optional[AffiliationsResponse] = None

    laboral: Optional[LaboralResponse] = None

    tallas: Optional[SizesResponse] = None

    archivos: List[FileResponse] = []