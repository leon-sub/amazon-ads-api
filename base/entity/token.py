from base.entity.base_entity import BaseEntity
from dataclasses import dataclass


@dataclass
class Token(BaseEntity):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
