import re

class Calculator:

    def add(self, a,b):
        return a + b

    def subtract(self, a,b):
        return a - b

    def divide(self, a,b):
        if b == 0:
            ZeroDivisionError()
        return a/b

    def multiply(self, a,b):
        return a * b

    def calculate(self, input):
        multiply = re.compile("(?P<first>[-]?[0-9]*[.]?[0-9]+)\\*(?P<second>[-]?[0-9]*[.]?[0-9]+)")
        divide = re.compile("(?P<first>[-]?[0-9]*[.]?[0-9]+)/(?P<second>[-]?[0-9]*[.]?[0-9]+)")
        plus = re.compile("(?P<first>[-]?[0-9]*[.]?[0-9]+)\\+(?P<second>[-]?[0-9]*[.]?[0-9]+)")
        minus = re.compile("(?P<first>[-]?[0-9]*[.]?[0-9]+)-(?P<second>[-]?[0-9]*[.]?[0-9]+)")

        while input.__contains__("*") or input.__contains__("/"):
            multiplymatch = re.match(multiply, input)
            dividematch = re.match(divide, input)
            if multiplymatch:
                a = float(multiplymatch.group(1))
                b = float(multiplymatch.group(2))
                out = self.multiply(a, b)
                input = re.sub(multiply, str(out), input, count=0)

            if dividematch:
                a = float(dividematch.group(1))
                b = float(dividematch.group(2))
                out = self.divide(a, b)
                input = re.sub(divide, str(out), input, count=0)

        while input.__contains__("+") or input.__contains__("-") and not input.startswith("-"):
            plusmatch = re.match(plus, input)
            minusmatch = re.match(minus, input)
            if plusmatch:
                a = float(plusmatch.group(1))
                b = float(plusmatch.group(2))
                out = self.add(a, b)
                input = re.sub(plus, str(out), input, count=0)

            if minusmatch:
                a = float(minusmatch.group(1))
                b = float(minusmatch.group(2))
                out = self.subtract(a, b)
                input = re.sub(minus, str(out), input, count=0)

        return float(input)

if __name__ == '__main__':
    asd = str(input())
    calc = Calculator()
    print(calc.calculate(asd))