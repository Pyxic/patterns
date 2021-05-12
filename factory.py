from abc import ABC, abstractmethod


class SocialNetworkPoster(ABC):

    @abstractmethod
    def get_social_network(self):
        pass

    def post(self, content):
        network = self.get_social_network()
        network.log_in()
        network.create_post(content)
        network.log_out()


class FacebookPoster(SocialNetworkPoster):

    def __init__(self, login, password):
        self.__login = login
        self.__password = password

    def get_social_network(self):
        return FacebookConnector(self.__login, self.__password)


class LinkedInPoster(SocialNetworkPoster):

    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def get_social_network(self):
        return LinkedInConnector(self.__email, self.__password)


class SocialNetworkConnector(ABC):

    @abstractmethod
    def log_in(self):
        pass

    @abstractmethod
    def log_out(self):
        pass

    @abstractmethod
    def create_post(self, content):
        pass


class FacebookConnector(SocialNetworkConnector):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def log_in(self):
        print(f"HTTP request to log in user {self.login} with password {self.password}")

    def log_out(self):
        print(f"HTTP request to logout user {self.login}")

    def create_post(self, content):
        print(f"HTTP request to create post in Facebook")


class LinkedInConnector(SocialNetworkConnector):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def log_in(self):
        print(f"HTTP request to log in user {self.email} with password {self.password}")

    def log_out(self):
        print(f"HTTP request to logout user {self.email}")

    def create_post(self, content):
        print(f"HTTP request to create post in LinkedIn")


def create_post(creator: SocialNetworkPoster, content):
    creator.post(content)


create_post(FacebookPoster('misha', 'password'), "hello world")
create_post(LinkedInPoster('mail@gmail.com', 'password'), "work")
