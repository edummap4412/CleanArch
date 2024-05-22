from typing import Dict
from source.domain.use_cases.user_finder import UserFinderInterface


class UserFinderSpy(UserFinderInterface):

    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, first_name: str) -> Dict:
        self.find_attributes['first_name'] = first_name

        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                {"first_name": first_name, "last_name": "something"}
            ]
        }