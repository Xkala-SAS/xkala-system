from pydantic import BaseModel


class SaveUserAddressRequest(
    BaseModel
):

    direccion: str

    barrio: str

    city_id: str