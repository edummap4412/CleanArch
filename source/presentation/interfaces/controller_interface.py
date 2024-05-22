from abc import ABC, abstractmethod
from source.presentation.http_types.http_requests import HttpRequest
from source.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
