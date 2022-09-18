from dataclasses import dataclass
from dataclasses import field
from typing import Optional

from app.services import BaseService
from users.models import User


@dataclass
class UserUpdater(BaseService):
    user: User
    password: str = ''
    new_user_data: dict = field(default_factory=dict)

    def act(self) -> None:
        self.update()

    def update(self) -> User:
        for key, value in self.new_user_data.items():
            setattr(self.user, key, value)

        self.set_password(self.user, self.password)
        self.user.save()

        return self.user

    def set_password(self, user: User, password: Optional[str]) -> None:
        if password:
            user.set_password(password)
