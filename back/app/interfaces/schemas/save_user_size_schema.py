from pydantic import BaseModel


class SaveUserSizeRequest(
    BaseModel
):

    shirt_size: str

    pants_size: str

    shoe_size: str