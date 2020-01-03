import unittest
from Calculator import Calculator
from parameterized import parameterized


class CalculatorTests(unittest.TestCase):
    calc = Calculator()

    @parameterized.expand([
        [2,2,4]
    ])
    def test_add_SimpleValuesShouldCalculate(self, x, y, expected):
        #Arrange
        #Act
        actual = self.calc.add(x,y)
        #Assert
        self.assertEqual(expected, actual)

    @parameterized.expand([
        [2, 2, 0]
    ])
    def test_subtract_SimpleValuesShouldCalculate(self, x, y, expected):
        #Arrange
        #Act
        actual = self.calc.subtract(x,y)
        #Assert
        self.assertEqual(expected,actual)

    @parameterized.expand([
        [2, 3, 6]
    ])
    def test_multiplication_SimpleValuesShouldCalculate(self, x, y, expected):
        #Arrange
        #Act
        actual = self.calc.multiply(x, y)
        #Assert
        self.assertEqual(expected, actual)

    @parameterized.expand([
        [2, 2, 1]
    ])
    def test_divide_SimpleValuesShouldCalculate(self, x, y, expected):
        #Arrange
        #Act
        actual = self.calc.divide(x, y)
        #Assert
        self.assertEqual(actual, expected)

    @parameterized.expand([
        [2]
    ])
    def test_divide_DivideByZero(self, x):
        #Arrange
        y = 0
        #Act
        #Assert
        self.assertRaises(ZeroDivisionError, self.calc.divide, x, y)



if __name__ == '__main__':
    unittest.main()
