from pydantic import BaseModel


class LoginRequest(BaseModel):

    numero_documento: str

    password: str


class RefreshTokenRequest(BaseModel):

    refresh_token: str