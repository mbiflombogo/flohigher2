#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", end=" ")
print("{} is {}".format(number, number % 10), end=" ")
if (number % 10) == 0:
    print("and is 0")
elif (number % 10) < 6 and (number % 10) != 0:
    print("and is less than 6 and not 0")
elif (number % 10) > 5:
    print("and is greater than 5")