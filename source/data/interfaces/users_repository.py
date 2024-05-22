from abc import ABC, abstractmethod
from source.domain.models.users import Users
from typing import List


class UserRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass

    @abstractmethod
    def select_user(self, first_name: str) -> List[Users]: pass
