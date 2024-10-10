def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))

    max = max_of_three(n1, n2, n3)
    print("Maximum of Three Numbers:", max)

except:
    print("Please enter valid numbers.")
