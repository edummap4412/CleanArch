from source.infra.db.settings.connection import DbConnectionHandler
from source.infra.db.entities.users import Users as UserEntity
from source.data.interfaces.users_repository import UserRepositoryInterface
from source.domain.models.users import Users
from typing import List


class UsersRepository(UserRepositoryInterface):
    @classmethod
    def insert_user(cls, *, first_name: str, last_name: str, age: int) -> None:
        with DbConnectionHandler() as database:
            try:
                new_registry = UserEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, *, first_name: str) -> List[Users]:
        with DbConnectionHandler() as database:
            try:
                users = (database.session.query(UserEntity).filter(UserEntity.first_name == first_name).all())
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception
