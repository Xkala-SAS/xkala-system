from pydantic import BaseModel


class UploadFileResponse(BaseModel):

    message: str

    path: str

    file_type: str