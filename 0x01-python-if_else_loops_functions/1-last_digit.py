#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#convert the number to absolute form
#Module by ten to get the last digit
digit = abs(number) % 10
if number < 0:
    digit = -digit
if digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif digit == 0:
    print("Last digit of {} is {} and is zero".format(number, digit))
elif digit <= 5:
    print("Last digit of {} is {} and is not less than 6 and not 0".format(number, digit))
