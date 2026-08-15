from datetime import datetime

from pydantic import BaseModel

from app.domain.user.enums.remuneration_type import (
    RemunerationType
)


class UpdateUserContractRequest(
    BaseModel
):

    position_id: str

    contract_type_id: str

    fecha_ingreso: datetime

    remuneration_type: RemunerationType

    remuneration_value: float

    estado_laboral: bool