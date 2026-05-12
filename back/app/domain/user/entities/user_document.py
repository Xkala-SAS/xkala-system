from app.domain.user.exceptions.user_validation_exceptions import (
    MissingDocumentException,
    MissingDocumentTypeException
)

class UserDocument:

    def __init__(
        self,
        user_id: str,
        numero_documento: str,
        document_type_id: str
    ):

        self.user_id = user_id

        self.numero_documento = numero_documento

        self.document_type_id = document_type_id

        self._validate()

    def _validate(self):

        if (
            not self.numero_documento
            or not self.numero_documento.strip()
        ):
            raise MissingDocumentException()

        if (
            not self.document_type_id
            or not self.document_type_id.strip()
        ):
            raise MissingDocumentTypeException()