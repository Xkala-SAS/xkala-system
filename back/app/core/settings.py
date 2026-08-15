import os

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


# ==========================================
# ENVIRONMENT
# ==========================================

ENV = os.getenv(
    "APP_ENV",
    "development"
)

if ENV not in [
    "development",
    "production"
]:
    raise ValueError(
        f"APP_ENV inválido: {ENV}"
    )


env_file = (
    ".env.prod"
    if ENV == "production"
    else ".env.dev"
)


# ==========================================
# SETTINGS
# ==========================================

class Settings(BaseSettings):

    # ======================================
    # APP
    # ======================================

    APP_NAME:str

    APP_ENV:str

    DEBUG:bool

    ROOT_PATH: str = ""
    PROXY_HEADERS: bool = True


    # ======================================
    # SECURITY
    # ======================================

    SECRET_KEY:str

    ALGORITHM:str

    ACCESS_TOKEN_EXPIRE_MINUTES:int

    REFRESH_TOKEN_EXPIRE_DAYS:int


    # ======================================
    # DATABASE
    # ======================================

    DB_HOST:str

    DB_PORT:int

    DB_USER:str

    DB_PASSWORD:str

    DB_NAME:str


    # ======================================
    # CORS
    # ======================================

    CORS_ORIGINS:str


    @property
    def cors_origins(self):

        return [

            origin.strip()

            for origin in self.CORS_ORIGINS.split(",")

        ]


    # ======================================
    # PROFILE FILES
    # ======================================

    PROFILE_ALLOWED_EXTENSIONS:list[str]=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]

    PROFILE_ALLOWED_MIME_TYPES:list[str]=[
        "image/jpeg",
        "image/png",
        "image/webp"
    ]

    PROFILE_MAX_SIZE_MB:int=5


    # ======================================
    # SIGNATURE FILES
    # ======================================

    SIGNATURE_ALLOWED_EXTENSIONS:list[str]=[
        "jpg",
        "jpeg",
        "png"
    ]

    SIGNATURE_ALLOWED_MIME_TYPES:list[str]=[
        "image/jpeg",
        "image/png"
    ]

    SIGNATURE_MAX_SIZE_MB:int=3


    # ======================================
    # DOCUMENT FILES
    # ======================================

    DOCUMENT_ALLOWED_EXTENSIONS:list[str]=[
        "pdf",
        "jpg",
        "jpeg",
        "png"
    ]

    DOCUMENT_ALLOWED_MIME_TYPES:list[str]=[
        "application/pdf",
        "image/jpeg",
        "image/png"
    ]

    DOCUMENT_MAX_SIZE_MB:int=10


    # ======================================
    # DATABASE URL
    # ======================================

    @property
    def DATABASE_URL(self):

        return (

            f"mysql+pymysql://"

            f"{self.DB_USER}:"

            f"{self.DB_PASSWORD}@"

            f"{self.DB_HOST}:"

            f"{self.DB_PORT}/"

            f"{self.DB_NAME}"

        )


    # ======================================
    # PYDANTIC CONFIG
    # ======================================

    model_config = SettingsConfigDict(
        extra="ignore"
    )


# ==========================================
# INSTANCE
# ==========================================

settings=Settings()