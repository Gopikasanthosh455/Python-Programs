def is_armstrong(num):
    sum = 0
    temp = num
    while num > 0:
        digit = num % 10
        sum += digit ** 3
        num //= 10
    return sum == temp
start = int(input("Enter the starting number of the interval: "))
end = int(input("Enter the ending number of the interval: "))

print(f"Armstrong numbers between ",start ,"and" ,end," are:")
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)
