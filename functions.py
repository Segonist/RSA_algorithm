from math import floor, sqrt
import random


def is_divisible(num1, num2):
    return num1 % num2 == 0


def lcm(a, b):
    return (a / gcd(a, b)) * b


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = floor(sqrt(number)) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True


def gen_prime(min_prime, max_prime):
    number = 0
    while not is_prime(number):
        number = random.randrange(min_prime, max_prime + 1)
    return number
