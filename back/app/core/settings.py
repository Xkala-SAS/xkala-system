import os

from pydantic_settings import BaseSettings


ENV = os.getenv(
    "APP_ENV",
    "development"
)


env_file = (
    ".env.prod"
    if ENV == "production"
    else ".env.dev"
)


class Settings(BaseSettings):

    APP_NAME: str

    APP_ENV: str

    DEBUG: bool

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DB_HOST: str

    DB_PORT: int

    DB_USER: str

    DB_PASSWORD: str

    DB_NAME: str

    CORS_ORIGINS: str

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

    class Config:

        env_file = env_file

        extra = "ignore"


settings = Settings()