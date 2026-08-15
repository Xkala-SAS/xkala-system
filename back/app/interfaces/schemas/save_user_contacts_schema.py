from pydantic import BaseModel


class ContactRequest(BaseModel):

    contact_type: str

    contact_value: str

    is_primary: bool = False


class SaveUserContactsRequest(BaseModel):

    contacts: list[ContactRequest]