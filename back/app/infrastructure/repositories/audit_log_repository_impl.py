from app.infrastructure.database.models.audit_log_model import (
    AuditLogModel
)


class AuditLogRepositoryImpl:

    def __init__(self, db):

        self.db = db

    def save(

        self,

        user_id=None,

        action=None,

        resource=None,

        method=None,

        endpoint=None,

        ip_address=None,

        user_agent=None,

        status_code=None,

        description=None,

        old_values=None,

        new_values=None,

        extra_data=None
    ):

        audit = AuditLogModel(

            user_id=user_id,

            action=action,

            resource=resource,

            method=method,

            endpoint=endpoint,

            ip_address=ip_address,

            user_agent=user_agent,

            status_code=status_code,

            description=description,

            old_values=old_values,

            new_values=new_values,

            extra_data=extra_data
        )

        self.db.add(audit)

        self.db.commit()

        self.db.refresh(audit)

        return audit