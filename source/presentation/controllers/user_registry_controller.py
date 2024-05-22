from source.presentation.http_types.http_requests import HttpRequest
from source.presentation.http_types.http_response import HttpResponse
from source.presentation.interfaces.controller_interface import ControllerInterface
from source.domain.use_cases.user_registry import UserRegistryInterface


class UserResgistryController(ControllerInterface):

    def __init__(self, use_case: UserRegistryInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        self.use_case.register(
            first_name=http_request.body['first_name'],
            last_name=http_request.body['last_name'],
            age=http_request.body['age']
        )

        return HttpResponse(
            body={'data': 'Usuario registrado com sucesso'},
            status_code=201
        )
