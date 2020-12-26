# python3
import random


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    remainder = n % 60
    if n <= 1:
        return n
    resultSum = fibo_sum_last_digit(remainder)
    return resultSum


def fibo_sum_last_digit(n):
    num = [0] * n
    num[0] = 1
    num[1] = 1
    for i in range(2, n):
        num[i] = (num[i - 2] + num[i - 1]) % 10
    return sum(num) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
