#23. Generate 3 random integers between 100 and 999 which is divisible by 5

import random


def random_integers():
    integers = []

    while len(integers) < 3:
        num = random.randint(100, 999)
        if num % 5 == 0:
            integers.append(num)
    return integers
result = random_integers()
print("Random integers divisible by 5:", result)
