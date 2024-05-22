from source.domain.models.users import Users
from source.domain.use_cases.user_finder import UserFinderInterface
from source.data.interfaces.users_repository import UserRepositoryInterface
from typing import Dict, List


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UserRepositoryInterface) -> None:
        self.users_repository = users_repository

    def find(self, first_name: str) -> Dict:

        self.__validation_name(first_name=first_name)

        users = self.__find_user(first_name=first_name)

        return self.__format_attributes(users=users)

    @classmethod
    def __validation_name(cls, *, first_name) -> None:
        if not first_name.isalpha():
            raise Exception("Nome invalido para a busca")

        if len(first_name) > 18:
            raise Exception("Nome muito grande para a busca")

    def __find_user(self, *, first_name) -> List[Users]:
        users = self.users_repository.select_user(first_name=first_name)
        if not users:
            raise Exception('Usuario nao encontrado')
        return users

    @classmethod
    def __format_attributes(cls, users: List[Users]) -> Dict:

        attributes = []
        for user in users:
            attributes.append({'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age})

        return {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }

