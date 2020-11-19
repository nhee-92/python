import figure
import unittest
import doctest
import coverage

def square_test():
    square = figure.Square()
    assert square.area(4,5) == 20
    assert square.get_diagonal(4,5) == 6.4031242374328485

def circle_test():
    circle = figure.Circle()
    assert circle.area(5) == 19.634954084936208
    assert circle.get_diagonal(8) == 8


square_test()
circle_test()

class Figure_test(unittest.TestCase):
    def set_up(self):
        self.square = figure.Square()
        self.circle = figure.Circle()

    def area(self):
        self.assertEquals(self.square.area(4,5) == 20)
        self.assertEquals(self.circle.area(5) == 19.634954084936208)

    def get_diagonal(self):
        self.assertEquals(self.square.get_diagonal(4,5) == 6.4031242374328485)
        self.assertEquals(self.circle.get_diagonal(8) == 8)

class Figure_doc_test:
    '''
    >>> square = figure.Square()
    >>> square.area(5,5)
    25
    '''

doctest.testmod()