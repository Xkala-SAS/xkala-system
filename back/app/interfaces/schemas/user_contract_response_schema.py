from datetime import datetime

from pydantic import BaseModel


class UserContractResponse(
    BaseModel
):

    id: str

    position_id: str

    position_name: str

    contract_type_id: str

    contract_type_name: str

    fecha_ingreso: datetime

    remuneration_type: str

    remuneration_value: float

    estado_laboral: bool