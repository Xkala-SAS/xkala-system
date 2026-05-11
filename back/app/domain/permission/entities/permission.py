from uuid import uuid4


class Permission:

    def __init__(
        self,
        codigo: str,
        descripcion: str = None,
        id: str = None
    ):

        self.id = id or str(uuid4())

        self.codigo = codigo
        self.descripcion = descripcion

        self._validate()

    def _validate(self):

        if not self.codigo:
            raise ValueError(
                "Código del permiso obligatorio"
            )