def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print("The sum of all numbers in the list is:", result)
