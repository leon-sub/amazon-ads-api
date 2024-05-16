from base.entity.base_entity import BaseEntity
from base.entity.configuration import Configuration
from dataclasses import dataclass


@dataclass
class Reports(BaseEntity):
    name: str
    startDate: str
    endDate: str
    configuration: Configuration
