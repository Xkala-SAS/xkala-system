import uuid

import shutil

from fastapi import UploadFile


def save_file(
    file: UploadFile,
    folder: str
):

    extension = (
        file.filename.split(".")[-1]
        .lower()
    )

    filename = (
        f"{uuid.uuid4()}.{extension}"
    )

    file_path = (
        f"uploads/{folder}/{filename}"
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return f"/uploads/{folder}/{filename}"