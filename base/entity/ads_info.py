from base.entity.base_entity import BaseEntity
from dataclasses import dataclass


@dataclass
class AdsInfo(BaseEntity):
    campaignId: str
    name: str
    startDate: str
    state: str
