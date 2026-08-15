from app.application.user.use_cases.save_personal_info import (
    SavePersonalInfoUseCase
)


class SavePersonalInfoService:

    def __init__(
        self,
        use_case: SavePersonalInfoUseCase
    ):
        self.use_case = use_case

    def execute(
        self,
        user_id: str,
        primer_nombre: str,
        segundo_nombre: str,
        primer_apellido: str,
        segundo_apellido: str,
        fecha_nacimiento,
        email: str,
        password: str
    ):

        return self.use_case.execute(

            user_id=user_id,

            primer_nombre=primer_nombre,

            segundo_nombre=segundo_nombre,

            primer_apellido=primer_apellido,

            segundo_apellido=segundo_apellido,

            fecha_nacimiento=fecha_nacimiento,

            email=email,

            password=password
        )