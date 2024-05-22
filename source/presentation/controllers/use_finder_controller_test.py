from source.presentation.controllers.user_finder_controller import UserFinderController
from source.data.test.user_finder_spy import UserFinderSpy


def test_use_finder_controller():
    class HttpRequestMock:
        def __init__(self):
            self.query_params = {'first_name': "first_name"}

    user_finder = UserFinderSpy()
    use_finder_controller = UserFinderController(user_finder)

    response = use_finder_controller.handle(HttpRequestMock())

    assert response.body['data']['attributes'][0]['first_name'] == 'first_name'
    assert response.status_code == 200

