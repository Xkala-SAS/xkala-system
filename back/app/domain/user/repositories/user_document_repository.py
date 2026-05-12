from abc import ABC, abstractmethod


class UserDocumentRepository(ABC):

    @abstractmethod
    def save(self, user_document):
        pass

    @abstractmethod
    def get_by_document(
        self,
        numero_documento: str
    ):
        pass