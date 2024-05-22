from abc import ABC, abstractmethod
from typing import Dict


class UserRegistryInterface(ABC):

    @abstractmethod
    def register(self, first_name: str, last_name: str, age: str) -> Dict:
        pass
