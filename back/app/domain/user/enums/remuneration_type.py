from enum import Enum


class RemunerationType(
    str,
    Enum
):

    MONTHLY = "MONTHLY"

    DAILY = "DAILY"

    HOURLY = "HOURLY"

    CONTRACT = "CONTRACT"