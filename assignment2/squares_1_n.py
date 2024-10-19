def list_squares(numbers):
    squares = []
    for i in numbers:
        squares.append(i**2)
    return squares

num= [1, 2, 3, 4, 5]
squares =list_squares(num)
print("List of squares:", squares)
