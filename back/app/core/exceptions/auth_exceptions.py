class InvalidCredentialsException(
    Exception
):

    def __init__(self):

        self.message = (
            "Credenciales inválidas"
        )

        super().__init__(
            self.message
        )


class InactiveUserException(
    Exception
):

    def __init__(self):

        self.message = (
            "Usuario inactivo"
        )

        super().__init__(
            self.message
        )