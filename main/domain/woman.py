from typing import List


class Woman:
    def __init__(self, name: str, preference_list: List[str]):
        self.name = name
        self.preference_list = preference_list

    def get_name(self):
        return self.name

    def get_preference_list(self):
        return self.preference_list

    @classmethod
    def from_json(cls, data):
        return cls(**data)