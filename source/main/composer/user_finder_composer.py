from source.infra.db.repositories.users_repository import UsersRepository
from source.data.use_cases.use_finder import UserFinder
from source.presentation.controllers.user_finder_controller import UserFinderController


def use_finder_composer():
    repository = UsersRepository()
    use_case = UserFinder(repository)
    controller = UserFinderController(use_case)
    return controller.handle
