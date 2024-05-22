import pytest

from source.data.use_cases.use_finder import UserFinder
from source.domain.models.users import Users
from source.infra.db.repositories.users_repository import UsersRepository
from source.tests.user_repository_mock import UsersRepositoryMock
from typing import List


def test_user_finder():
    repo = UsersRepository()
    user_finder = UserFinder(repo)

    response = user_finder.find('first')

    print(response)


def test_user_finder_with_class_mock():

    repo = UsersRepositoryMock()
    user_finder = UserFinder(repo)

    response = user_finder.find('first')
    assert response['attributes'][0]['first_name'] == 'first'


def test_find_error_user_not_found():
    class UserRepositoryError(UsersRepositoryMock):
        def select_user(self, *, first_name: str) -> List[Users]:
            return []

    with pytest.raises(Exception, match="Usuario nao encontrado"):
        first_name = 'meuNome'

        repo = UserRepositoryError()
        user_finder = UserFinder(repo)
        user_finder.find(first_name=first_name)


def test_max_legth_name():
    with pytest.raises(Exception, match="Nome muito grande para a busca"):
        first_name = 'qipweqwoeqwoiqwueoiqwueqowieuqwoieuqwiodjqwoidjqwoidjq'

        repo = UsersRepositoryMock()
        user_finder = UserFinder(repo)
        user_finder.find(first_name=first_name)

