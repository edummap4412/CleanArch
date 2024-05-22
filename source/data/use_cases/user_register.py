from source.data.interfaces.users_repository import UserRepositoryInterface
from source.domain.use_cases.user_registry import UserRegistryInterface
from typing import Dict


class UserRegistry(UserRegistryInterface):
    def __init__(self, users_repository: UserRepositoryInterface):
        self.__users_repository = users_repository

    def register(self, *, first_name: str, last_name: str, age: int) -> Dict:
        self.__validation_name(names=first_name)
        self.__validation_name(names=last_name)

        self.__registry_user(first_name=first_name, last_name=last_name, age=age)
        response = self.__format_attributes(first_name=first_name, last_name=last_name, age=age)
        return response

    @classmethod
    def __validation_name(cls, *, names: str) -> None:
        if not names.isalpha():
            raise Exception("Nome invalido para a busca")

        if len(names) > 18:
            raise Exception("Nome muito grande para a busca")

    def __registry_user(self, *, first_name: str, last_name: str, age: int) -> None:
        self.__users_repository.insert_user(first_name=first_name, last_name=last_name, age=age)

    @classmethod
    def __format_attributes(cls, *,  first_name: str, last_name: str, age: int) -> Dict:
        return {
            "type": "Users",
            "count": '1',
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
