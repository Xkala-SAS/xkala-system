from fastapi import (
    UploadFile,
    HTTPException
)

from app.core.settings import (
    settings
)


class FileValidator:

    @staticmethod
    def validate_file(

        file: UploadFile,

        allowed_extensions: list[str],

        allowed_mime_types: list[str],

        max_size_mb: int
    ):

        # ==============================
        # VALIDAR NOMBRE
        # ==============================

        if not file.filename:

            raise HTTPException(

                status_code=400,

                detail="Archivo inválido"
            )

        # ==============================
        # VALIDAR EXTENSIÓN
        # ==============================

        extension = (
            file.filename
            .split(".")[-1]
            .lower()
        )

        if extension not in allowed_extensions:

            raise HTTPException(

                status_code=400,

                detail=(
                    "Extensión no permitida"
                )
            )

        # ==============================
        # VALIDAR MIME TYPE
        # ==============================

        if file.content_type not in allowed_mime_types:

            raise HTTPException(

                status_code=400,

                detail=(
                    "Tipo de archivo inválido"
                )
            )

        # ==============================
        # VALIDAR TAMAÑO
        # ==============================

        file.file.seek(0, 2)

        size = file.file.tell()

        file.file.seek(0)

        max_size = (
            max_size_mb
            * 1024
            * 1024
        )

        if size > max_size:

            raise HTTPException(

                status_code=400,

                detail=(
                    f"Archivo supera "
                    f"{max_size_mb}MB"
                )
            )

    # ==================================
    # PROFILE PHOTO
    # ==================================

    @staticmethod
    def validate_profile_photo(
        file: UploadFile
    ):

        FileValidator.validate_file(

            file=file,

            allowed_extensions=
                settings.PROFILE_ALLOWED_EXTENSIONS,

            allowed_mime_types=
                settings.PROFILE_ALLOWED_MIME_TYPES,

            max_size_mb=
                settings.PROFILE_MAX_SIZE_MB
        )

    # ==================================
    # SIGNATURE
    # ==================================

    @staticmethod
    def validate_signature(
        file: UploadFile
    ):

        FileValidator.validate_file(

            file=file,

            allowed_extensions=
                settings.SIGNATURE_ALLOWED_EXTENSIONS,

            allowed_mime_types=
                settings.SIGNATURE_ALLOWED_MIME_TYPES,

            max_size_mb=
                settings.SIGNATURE_MAX_SIZE_MB
        )

    @staticmethod
    def validate_document(
        file: UploadFile
    ):
    
        # ==============================
        # VALIDAR EXTENSIÓN
        # ==============================
    
        extension = (
            file.filename
            .split(".")[-1]
            .lower()
        )
    
        if (
            extension
            not in settings.DOCUMENT_ALLOWED_EXTENSIONS
        ):
    
            raise HTTPException(
            
                status_code=400,
    
                detail="Formato no permitido"
            )
    
        # ==============================
        # VALIDAR MIME TYPE
        # ==============================
    
        if (
            file.content_type
            not in settings
            .DOCUMENT_ALLOWED_MIME_TYPES
        ):
    
            raise HTTPException(
            
                status_code=400,
    
                detail="MIME TYPE no permitido"
            )
    
        # ==============================
        # VALIDAR TAMAÑO
        # ==============================
    
        file.file.seek(0, 2)
    
        size = file.file.tell()
    
        file.file.seek(0)
    
        max_size = (
            settings.DOCUMENT_MAX_SIZE_MB
            * 1024
            * 1024
        )
    
        if size > max_size:
        
            raise HTTPException(
            
                status_code=400,
    
                detail=(
                    f"Archivo supera "
                    f"{settings.DOCUMENT_MAX_SIZE_MB}MB"
                )
            )