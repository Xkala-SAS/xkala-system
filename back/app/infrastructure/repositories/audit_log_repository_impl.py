from sqlalchemy.orm import Session

from app.infrastructure.database.models.audit_log_model import (
    AuditLogModel
)


class AuditLogRepositoryImpl:

    def __init__(self, db: Session):

        self.db = db

    def save(self, audit_log):

        self.db.add(audit_log)

        self.db.commit()

        self.db.refresh(audit_log)

        return audit_log