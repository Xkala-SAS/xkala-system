from enum import Enum


class UserFileType(str, Enum):

    PROFILE_PHOTO = "profile_photo"

    SIGNATURE = "signature"

    CEDULA = "cedula"

    RUT = "rut"

    CONTRACT = "contract"

    EPS_CERTIFICATE = (
        "eps_certificate"
    )

    ARL_CERTIFICATE = (
        "arl_certificate"
    )

    PENSION_CERTIFICATE = (
        "pension_certificate"
    )

    CESANTIAS_CERTIFICATE = (
        "cesantias_certificate"
    )

    LABOR_CERTIFICATE = (
        "labor_certificate"
    )