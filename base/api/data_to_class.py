def json_to_class(json: dict, cls) -> object:
    return cls.from_json(json)
