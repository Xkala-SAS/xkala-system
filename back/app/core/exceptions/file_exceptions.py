class InvalidFileExtensionException(
    Exception
):

    def __init__(self):

        self.message = (
            "Formato no permitido"
        )

        super().__init__(
            self.message
        )


class FileTooLargeException(
    Exception
):

    def __init__(self):

        self.message = (
            "Archivo demasiado grande"
        )

        super().__init__(
            self.message
        )