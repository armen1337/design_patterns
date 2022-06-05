from abc import ABC, abstractmethod


class User:
    def __init__(self, username: str, password: str, role: str):
        """
        :param role: Available options: ["user", "admin", "super_admin"]
        """
        self._username = username
        self._pwd = password
        self._role = role

    @property
    def username(self) -> str:
        return self._username

    @property
    def role(self) -> str:
        return self._role


class AbstractHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, user: User) -> str:
        pass


class Handler(AbstractHandler, ABC):
    _next_handler: AbstractHandler = None

    def set_next(self, handler: AbstractHandler) -> AbstractHandler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, user: User) -> str:  # Default handle method to return 'None' if there's no match
        if self._next_handler is not None:
            return self._next_handler.handle(user)
        return None


class UserHandler(Handler):
    def handle(self, user: User) -> str:
        if user.role == "user":
            return f"User '{user.username}' can read posts"
        return super().handle(user)


class AdminHandler(Handler):
    def handle(self, user: User) -> str:
        if user.role == "admin":
            return f"User '{user.username}' can create posts"
        return super().handle(user)


class SuperAdminHandler(Handler):
    def handle(self, user: User) -> str:
        if user.role == "super_admin":
            return f"User '{user.username}' can create admins"
        return super().handle(user)


if __name__ == '__main__':
    # User definitions
    user = User("i_am_user", "pwd", "user")
    admin = User("i_am_admin", "pwd", "admin")
    super_admin = User("i_am_super_admin", "pwd", "super_admin")

    # Handler definitions
    user_handler = UserHandler()
    admin_handler = AdminHandler()
    super_admin_handler = SuperAdminHandler()

    # Code usage
    user_handler.set_next(admin_handler).set_next(super_admin_handler)

    print(user_handler.handle(user))
    print(user_handler.handle(admin))
    print(user_handler.handle(super_admin))

    print(super_admin_handler.handle(user))  # Negative case - None

