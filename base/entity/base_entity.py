from dataclasses import dataclass, fields


@dataclass
class BaseEntity:
    def to_dict(self) -> dict:
        attributes = self.__dict__
        return {k: v for k, v in attributes.items()}

    @classmethod
    def from_json(cls, json_data):
        data = {i.name: json_data[i.name] for i in fields(cls)}
        return cls(**data)
