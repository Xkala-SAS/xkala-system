from app.infrastructure.database.models.user_file_model import (
    UserFileModel
)


class ListUserDocumentsService:

    def __init__(self, repository):

        self.repository = repository

    def execute(self, user_id):

        documents = (
            self.repository
            .get_user_files(user_id)
        )

        result = []

        for document in documents:

            result.append({

                "id":
                    str(document.id),

                "file_type":
                    document.file_type,

                "file_path":
                    document.file_path,

                "uploaded_at":
                    document.uploaded_at,

                "is_active":
                    document.is_active,

                "is_primary":
                    document.is_primary
            })

        return result