class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

obj= Calculator()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", obj.add(num1, num2))
print("Subtraction:", obj.subtract(num1, num2))
print("Multiplication:",obj.multiply(num1, num2))
print("Division:", obj.divide(num1, num2))
