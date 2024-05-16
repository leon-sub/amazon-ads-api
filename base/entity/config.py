from base.entity.base_entity import BaseEntity
from dataclasses import dataclass


@dataclass
class Config(BaseEntity):
    client_id: str
    client_secret: str
    refresh_token: str
    scope_code: str