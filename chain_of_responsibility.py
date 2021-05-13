import sys
from abc import ABC
from datetime import datetime, timedelta


class Middleware(ABC):

    _next = None

    def link_with(self, next):
        self._next = next
        return next

    def check(self, email, password):
        if not self._next:
            return None
        return self._next.check(email, password)


class UserExistsMiddleware(Middleware):

    def __init__(self, server):
        self.__server = server

    def check(self, email, password):
        print(self.__server.has_email(email))
        if not self.__server.has_email(email):
            print("UserExistsMiddleware: This email is not registered!")
        if not self.__server.is_valid_password(email, password):
            print("UserExistsMiddleware: Wrong password!")
            return False
        return super().check(email, password)


class RoleCheckMiddleware(Middleware):

    def check(self, email, password):
        if email == 'admin@gmail.com':
            print("RoleCheckMiddleware: Hello, admin!")
            return True
        print("RoleCheckMiddleware: Hello, user!\n")
        return super().check(email, password)


class ThrottlingMiddleware(Middleware):

    __request_per_minute = None
    __request = 0
    __currentTime = 0

    def __init__(self, request_per_minute):
        self.__request_per_minute = request_per_minute
        self.__currentTime = datetime.now()

    def check(self, email, password):
        if datetime.now() > self.__currentTime+timedelta(minutes=1):
            self.__request = 0
            self.__currentTime = datetime()

        self.__request += 1
        if self.__request > self.__request_per_minute:
            print("ThrottlingMiddleware: Request limit exceeded!")
            sys.exit()

        return super().check(email, password)


class Server:
    __users = {}
    __middleware = None

    def set_middleware(self, middleware: Middleware):
        self.__middleware = middleware

    def log_in(self, email, password):
        if self.__middleware.check(email, password):
            print("Server: Authorization has been successful!")
            return True
        return False

    def register(self, email, password):
        self.__users[email] = password

    def has_email(self, email):
        return email in self.__users

    def is_valid_password(self, email, password):
        return self.has_email(email) and self.__users[email] == password


server = Server()
server.register('admin@gmail.com', 'pass12345')
server.register('user@gmail.com', '12345')
middleware = ThrottlingMiddleware(2)
user_exit_middleware = UserExistsMiddleware(server)
role_middleware = RoleCheckMiddleware()

middleware.link_with(user_exit_middleware).link_with(role_middleware)

server.set_middleware(middleware)

success = False
while not success:
    print("\nEnter your email:\n")
    email = input()
    print("Enter your password:\n")
    password = input()
    success = server.log_in(email, password)

