from pydantic import BaseModel


class SaveUserHealthInfoRequest(
    BaseModel
):

    eps_id: str

    arl_id: str

    pension_fund_id: str

    severance_fund_id: str