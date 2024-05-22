from source.infra.db.repositories.users_repository import UsersRepository
from source.data.use_cases.user_register import UserRegistry
from source.presentation.controllers.user_registry_controller import UserResgistryController


def use_register_composer():
    repository = UsersRepository()
    use_case = UserRegistry(repository)
    controller = UserResgistryController(use_case)

    return controller.handle

