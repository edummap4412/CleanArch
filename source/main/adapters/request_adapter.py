from typing import Callable
from flask import request as flask_request
from source.presentation.http_types.http_requests import HttpRequest
from source.presentation.http_types.http_response import HttpResponse


def request_adapter(request: flask_request, controller: Callable) -> HttpResponse:
    body = None
    if request.data:
        body = request.json

    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )

    http_response = controller(http_request)
    return http_response
