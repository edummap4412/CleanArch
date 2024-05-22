from source.domain.use_cases.user_registry import UserRegistryInterface
from typing import Dict


class UserRegistrySpy(UserRegistryInterface):
    def __init__(self):
        self.register_attributes = {}

    def register(self, first_name: str, last_name: str, age: str) -> None:
        self.register_attributes['first_name'] = first_name,
        self.register_attributes['last_name'] = last_name,
        self.register_attributes['age'] = age
        return
