from base.entity.base_entity import BaseEntity
from base.entity.account_info import AccountInfo
from dataclasses import dataclass


@dataclass
class ProFile(BaseEntity):
    profileId: int
    countryCode: str
    currencyCode: str
    dailyBudget: float
    timezone: str
    accountInfo: AccountInfo

    @classmethod
    def from_json(cls, json_data):
        def _convert(obj):
            class_type = globals()["AccountInfo"]
            obj["accountInfo"] = class_type(**obj["accountInfo"])
            return obj

        return cls(**_convert(json_data))
