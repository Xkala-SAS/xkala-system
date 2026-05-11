from pydantic_settings import BaseSettings


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

    class Config:
        env_file = ".env"

    @property
    def DATABASE_URL(self):
        return (
            f"mysql+pymysql://"
            f"{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()