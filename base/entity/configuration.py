from base.entity.base_entity import BaseEntity
from dataclasses import dataclass


@dataclass
class Configuration(BaseEntity):
    adProduct: str
    groupBy: list
    columns: list
    reportTypeId: str
    timeUnit: str
    format: str = "GZIP_JSON"
