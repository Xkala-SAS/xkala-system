from uuid import uuid4


class Role:

    def __init__(
        self,
        nombre: str,
        descripcion: str = None,
        id: str = None
    ):

        self.id = id or str(uuid4())
        self.nombre = nombre
        self.descripcion = descripcion

        self._validate()

    def _validate(self):

        if not self.nombre:
            raise ValueError("Nombre del rol obligatorio")