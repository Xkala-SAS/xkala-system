import os

import uuid

import shutil

from fastapi import UploadFile


def save_file(
    file: UploadFile,
    folder: str
):

    # extensión
    extension = (
        file.filename
        .split(".")[-1]
        .lower()
    )

    # nombre único
    filename = (
        f"{uuid.uuid4()}.{extension}"
    )

    # carpeta física
    upload_dir = (
        f"uploads/{folder}"
    )

    # crear carpetas si no existen
    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    # ruta física
    file_path = (
        f"{upload_dir}/{filename}"
    )

    # guardar archivo
    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # url pública
    return (
        f"/uploads/{folder}/{filename}"
    )