from abc import ABC, abstractmethod


class Entity(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


class Company(Entity):

    def __init__(self, name, departments: list):
        self.__name = name
        self.__departments =departments

    @property
    def name(self):
        return self.__name

    @property
    def departments(self):
        return self.__departments

    def accept(self, visitor):
        return visitor.visit_company(self)


class Department(Entity):

    def __init__(self, name, employees):
        self.__name = name
        self.__employees = employees

    @property
    def name(self):
        return self.__name

    @property
    def employees(self):
        return self.__employees

    def get_cost(self):
        cost = 0
        for employee in self.__employees:
            cost += employee.salary
        return cost

    def accept(self, visitor):
        return visitor.visit_department(self)


class Employee(Entity):

    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    def accept(self, visitor):
        return visitor.visit_employee(self)


class Visitor(ABC):

    @abstractmethod
    def visit_company(self, company: Company):
        pass

    @abstractmethod
    def visit_department(self, department: Department):
        pass

    @abstractmethod
    def visit_employee(self, employee: Employee):
        pass


class SalaryReport(Visitor):

    def visit_company(self, company: Company):
        output = ""
        total = 0

        for department in company.departments:
            total += department.get_cost()
            output += "\n--" + self.visit_department(department)

        output = company.name + f"({total})\n" + output

        return output

    def visit_department(self, department: Department):
        output = ""

        for employee in department.employees:
            output += " " + self.visit_employee(employee)

        output = department.name + f"({department.get_cost()})\n" + output

        return output

    def visit_employee(self, employee: Employee):

        return str(employee.salary) + " " + employee.name + " " + employee.position + "\n"


mobile_dev = Department("Mobile Development", [
    Employee("Albert Falmore", "designer", 100000),
    Employee("Ali Halabay", "programmer", 100000),
    Employee("Sarah Konor", "programmer", 90000),
    Employee("Monica Ronaldino", "QA engineer", 31000),
    Employee("James Smith", "QA engineer", 30000),
])

tech_support = Department("Tech Support", [
    Employee("Larry Ulbrecht", "supervisor", 70000),
    Employee("Elton Pale", "operator", 30000),
    Employee("Rajeet Kumar", "operator", 30000),
    Employee("John Burnovsky", "operator", 34000),
    Employee("Sergey Korolev", "operator", 35000),
])

company = Company("SuperStarDevelopment", [mobile_dev, tech_support])

report = SalaryReport()

print(company.accept(report))

print(tech_support.accept(report))
