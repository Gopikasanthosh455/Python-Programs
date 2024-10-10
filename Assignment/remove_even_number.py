my_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]
odd_numbers = []
for number in my_list:
    if number % 2 != 0:
        odd_numbers.append(number)
print("Numbers after removing even numbers:", odd_numbers)
