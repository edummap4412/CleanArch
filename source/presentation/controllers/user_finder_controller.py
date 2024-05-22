from source.presentation.http_types.http_requests import HttpRequest
from source.presentation.http_types.http_response import HttpResponse
from source.presentation.interfaces.controller_interface import ControllerInterface
from source.domain.use_cases.user_finder import UserFinderInterface


class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params['first_name']
        response = self.use_case.find(first_name)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )

