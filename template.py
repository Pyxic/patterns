from abc import ABC, abstractmethod
from time import sleep


class SocialNetwork(ABC):

    def __init__(self, username, password):
        self._username = username
        self._password = password

    def post(self, message):
        if self.log_in(self._username, self._password):
            result = self.send_data(message)
            self.log_out()
            return result
        return False

    @abstractmethod
    def log_in(self, username, password):
        pass

    @abstractmethod
    def send_data(self, message):
        pass

    @abstractmethod
    def log_out(self):
        pass


class Facebook(SocialNetwork):

    def log_in(self, username, password):
        print("\nChecking user's credentials...\n")
        print("name: "+self._username)
        print("Password: "+"*"*len(self._password) + "\n")

        simulateNetworkLatency()
        print(f"facebook: {self._username} has logged in successfully")

        return True

    def send_data(self, message):
        print(f"facebook: user {self._username} has posted message: {message}")
        return True

    def log_out(self):
        print(f"facebook: user {self._username} has been logged out")


class Twitter(SocialNetwork):
    def log_in(self, username, password):
        print("\nChecking user's credentials...\n")
        print("name: " + self._username)
        print("Password: " + "*" * len(self._password) + "\n")

        simulateNetworkLatency()
        print(f"twitter: {self._username} has logged in successfully")

        return True

    def send_data(self, message):
        print(f"twitter: user {self._username} has posted message: {message}")
        return True

    def log_out(self):
        print(f"twitter: user {self._username} has been logged out")


def simulateNetworkLatency():
    for _ in range(5):
        print('.')
        sleep(1)


network1 = Facebook("misha", '12345')
network1.post("message")

network2 = Twitter("Sasha", 'pass12345')
network2.post("messsage")

