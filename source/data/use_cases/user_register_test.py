from source.tests.user_repository_mock import UsersRepositoryMock
from .user_register import UserRegistry


def test_register():
    first_name = 'ola'
    last_name = 'aqui'
    age = 3

    repo = UsersRepositoryMock()
    user_register = UserRegistry(repo)

    response = user_register.register(first_name=first_name, last_name=last_name, age=age)

    assert repo.insert_user_attributes['first_name'] == first_name
    assert repo.insert_user_attributes['last_name'] == last_name
    assert repo.insert_user_attributes['age'] == age

    assert response['type'] == "Users"
    assert response['count'] == '1'
    assert response['attributes']
