import abc
import math

class Figure(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        pass
    
    @abc.abstractmethod
    def get_diagonal(self):
        pass


class Square(Figure):
    def __init__(self):
        super().__init__()

    def area(self, a, b):
        self.result = a * b

        return self.result

    def get_diagonal(self, a, b):
        self.result = math.sqrt(a * a + b * b)

        return self.result

class Circle(Figure):
    def __init__(self):
        super().__init__()

    def area(self, d):
        self.r = d / 2
        self.result = self.r * self.r * math.pi
        return self.result

    def get_diagonal(self, d):
        return d

