from abc import abstractmethod, ABC


class Department:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nome):
        self.__name = nome

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.__hours = 8

    @abstractmethod
    def calc_bonus(self):
        raise NotImplementedError("Não implementado")

    @abstractmethod
    def get_hours(self):
        raise NotImplementedError("Não implementado")

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    @property
    def salary(self):
        return self.__salary

    @property
    def hours(self):
        return self.__hours

    @name.setter
    def name(self, name):
        self.__name = name

    @code.setter
    def code(self, code):
        self.__code = code

    @salary.setter
    def salary(self, salary):
        self.__salary = salary


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, departamento):
        self.__departament = departamento


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales__ = 0

    def get_sales(self):
        return self.__sales__

    def put_sales(self, sale):
        self.__sales__ += sale

    def get_hours(self):
        return self.hours

    def calc_bonus(self):
        return self.__sales__ * 0.15

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, departamento):
        self.__departament = departamento


