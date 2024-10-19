def multiply(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product

numbers = [2, 3, 4, 5]
result = multiply(numbers)
print("The product of all numbers in the list is:", result)
