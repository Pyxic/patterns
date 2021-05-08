from abc import ABC, abstractmethod


class Project(ABC):

    @abstractmethod
    def run(self):
        pass


class RealProject(Project):
    __url = ''

    def __init__(self, url):
        self.__url = url
        self.load()

    def load(self):
        print(f"load project from {self.__url}")

    def run(self):
        print("run project")


class ProxyProject(Project):
    __url = ''
    __real_project = None

    def __init__(self, url):
        self.__url = url

    def run(self):
        if self.__real_project is None:
            self.__real_project = RealProject(self.__url)
        self.__real_project.run()


project = ProxyProject("https://www.github.com/user/project")

project.run()
