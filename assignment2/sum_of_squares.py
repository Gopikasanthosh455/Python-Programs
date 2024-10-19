n = int(input("Enter a positive integer : "))
sum_of_squares = 0

for i in range(1, n + 1):
    sum_of_squares += i ** 2

print("The sum of squares of the first", n, "natural numbers is:", sum_of_squares)
