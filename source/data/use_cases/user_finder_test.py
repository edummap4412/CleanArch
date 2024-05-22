from source.data.use_cases.use_finder import UserFinder
from source.infra.db.repositories.users_repository import UsersRepository


def test_find():
    repo = UsersRepository()
    user_finder = UserFinder(repo)
