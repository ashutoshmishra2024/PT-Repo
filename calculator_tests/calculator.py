class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    #divide
    def divide(self, a, b):
        if b == 0:
            raise ValueError("cannot divide by zero")
        return a / b