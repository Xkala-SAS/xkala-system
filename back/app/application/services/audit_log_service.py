from app.infrastructure.database.models.audit_log_model import (
    AuditLogModel
)


class AuditLogService:

    def __init__(self, repository):

        self.repository = repository

    def execute(

        self,

        user_id: str,

        action: str,

        resource: str,

        method: str,

        endpoint: str,

        ip_address: str
    ):

        audit_log = AuditLogModel(

            user_id=user_id,

            action=action,

            resource=resource,

            method=method,

            endpoint=endpoint,

            ip_address=ip_address
        )

        return self.repository.save(
            audit_log
        )