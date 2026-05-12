from datetime import (
    datetime,
    timedelta,
    timezone
)

from uuid import uuid4

from jose import (
    jwt,
    JWTError,
    ExpiredSignatureError
)

from app.core.settings import settings

from app.core.exceptions.base_exception import (
    AppException
)


class JWTHandler:

    @staticmethod
    def create_access_token(
        data: dict
    ) -> str:

        now = datetime.now(
            timezone.utc
        )

        expire = now + timedelta(
            minutes=(
                settings
                .ACCESS_TOKEN_EXPIRE_MINUTES
            )
        )

        to_encode = data.copy()

        to_encode.update({

            "iat": now,

            "exp": expire,

            "jti": str(uuid4()),

            "token_type": "access"
        })

        token = jwt.encode(

            to_encode,

            settings.SECRET_KEY,

            algorithm=settings.ALGORITHM
        )

        return token

    @staticmethod
    def decode_token(
        token: str
    ) -> dict:

        try:

            payload = jwt.decode(

                token,

                settings.SECRET_KEY,

                algorithms=[
                    settings.ALGORITHM
                ]
            )

            return payload

        except ExpiredSignatureError:

            raise AppException(

                message="Token expirado",

                status_code=401,

                error_code="TOKEN_EXPIRED"
            )

        except JWTError:

            raise AppException(

                message="Token inválido",

                status_code=401,

                error_code="INVALID_TOKEN"
            )