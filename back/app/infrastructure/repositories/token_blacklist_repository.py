from app.infrastructure.database.models.token_blacklist_model import (
    TokenBlacklistModel
)


class TokenBlacklistRepository:

    def __init__(self, db):

        self.db = db

    # ==========================================
    # ADD TOKEN
    # ==========================================

    def add(

        self,

        jti,

        token_type,

        expires_at
    ):

        token = TokenBlacklistModel(

            jti=jti,

            token_type=token_type,

            expires_at=expires_at
        )

        self.db.add(token)

        self.db.commit()

    # ==========================================
    # IS BLACKLISTED
    # ==========================================

    def exists(self, jti):

        return (

            self.db
            .query(TokenBlacklistModel)
            .filter(
                TokenBlacklistModel.jti == jti
            )
            .first()
            is not None
        )