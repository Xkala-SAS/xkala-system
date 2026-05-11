from fastapi import UploadFile

from app.core.settings import settings

from app.core.exceptions.file_exceptions import (
    InvalidFileExtensionException,
    FileTooLargeException
)


class FileValidator:

    @staticmethod
    def validate_profile_photo(
        file: UploadFile
    ):

        contents = file.file.read()

        extension = (
            file.filename
            .split(".")[-1]
            .lower()
        )

        # reset stream
        file.file.seek(0)

        # validar extensión
        if extension not in (
            settings.PROFILE_ALLOWED_EXTENSIONS
        ):

            raise (
                InvalidFileExtensionException()
            )

        # validar tamaño
        if len(contents) > (
            settings.MAX_FILE_SIZE
        ):

            raise FileTooLargeException()