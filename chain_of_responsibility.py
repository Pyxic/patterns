import sys
from abc import ABC
from datetime import datetime, timedelta


class Middleware(ABC):
    _next = None

    def link_to_next(self, next):
        self._next = next
        return next

    def check(self, email, password):
        if not self._next:
            return None
        return self._next.check(email, password)


class UserExistsMiddleware(Middleware):

    def __init__(self, server):
        self._server = server

    def check(self, email, password):
        if not self._server.has_email(email):
            print("Authorization: email does not exists")
        if not self._server.has_password(email, password):
            print("Authorization: wrong password")
            return False
        return super().check(email, password)


class RoleCheckMiddleware(Middleware):

    def check(self, email, password):
        if email == 'admin@gmail.com':
            print("RoleCheckMiddleware: Hello, admin!")
            return True
        print("RoleCheckMiddleware: Hello, user!")
        return True


class ThrottlingMiddleware(Middleware):
    __request_per_minute = None
    __request = 0
    __initial_time = 0

    def __init__(self, request_per_minute):
        self.__request_per_minute = request_per_minute
        self.__initial_time = datetime.now()

    def check(self, email, password):
        if datetime.now() > self.__initial_time+timedelta(minutes=2):
            self.__request = 0
            self.__initial_time = datetime()

        self.__request += 1
        if self.__request > self.__request_per_minute:
            print("ThrottlingMiddleware: Request limit exceeded!")
            sys.exit()

        return super().check(email, password)


class Server:

    _users = {}
    _middleware = None

    def set_middleware(self, middleware):
        self._middleware = middleware

    def log_in(self, email, password):
        if self._middleware.check(email, password):
            print("Authorization has been successful")
            return True
        return False

    def register(self, email, password):
        self._users[email] = password

    def has_email(self, email):
        return email in self._users

    def has_password(self, email, password):
        if self.has_email(email) and self._users[email] == password:
            return True
        return False


server = Server()
server.register('admin@gmail.com', 'pass12345')
server.register('some_user@gmail.com', '12345')
middleware = ThrottlingMiddleware(4)
user_exit_middleware = UserExistsMiddleware(server)
role_middleware = RoleCheckMiddleware()

middleware.link_to_next(user_exit_middleware).link_to_next(role_middleware)

server.set_middleware(middleware)

success = False
while not success:
    print("\nEnter your email:\n")
    email = input()
    print("Enter your password:\n")
    password = input()
    success = server.log_in(email, password)
