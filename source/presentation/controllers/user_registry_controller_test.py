from source.data.test.uer_registry_spy import UserRegistrySpy
from source.presentation.controllers.user_registry_controller import UserResgistryController


def test_user_registry_controller():
    class HttpRequestMock:
        def __init__(self):
            self.body = {
                'first_name': 'first_name',
                'last_name': 'last_name',
                'age': 'age'
            }
    use_registry_spy = UserRegistrySpy()
    user_registry_controller = UserResgistryController(use_registry_spy)

    response = user_registry_controller.handle(HttpRequestMock())

    assert response.body['data'] == 'Usuario registrado com sucesso'
    assert response.status_code == 201
