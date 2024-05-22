from source.domain.models.users import Users
from typing import List
from source.data.interfaces.users_repository import UserRepositoryInterface


class UsersRepositoryMock(UserRepositoryInterface):

    def __init__(self):
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, *, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age
        return

    def select_user(self, *, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name
        users = [Users(id='10', first_name='first', last_name='last', age='23'),
                 Users(id='11', first_name='first', last_name='last', age='53')]
        return users

