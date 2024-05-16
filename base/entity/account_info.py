from base.entity.base_entity import BaseEntity
from dataclasses import dataclass


@dataclass
class AccountInfo(BaseEntity):
    marketplaceStringId: str
    id: str
    type: str
    name: str
    validPaymentMethod: bool
