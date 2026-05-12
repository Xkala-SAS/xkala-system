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

    APP_NAME: str

    APP_ENV: str

    DEBUG: bool


    # ======================================
    # SECURITY
    # ======================================

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int


    # ======================================
    # DATABASE
    # ======================================

    DB_HOST: str

    DB_PORT: int

    DB_USER: str

    DB_PASSWORD: str

    DB_NAME: str


    # ======================================
    # CORS
    # ======================================

    CORS_ORIGINS: str


    # ======================================
    # DATABASE URL
    # ======================================

    @property
    def DATABASE_URL(self) -> str:

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

        env_file=env_file,

        extra="ignore"
    )


# ==========================================
# INSTANCE
# ==========================================

settings = Settings()