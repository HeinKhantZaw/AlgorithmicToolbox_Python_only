# python3
import math


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    remainder = from_index % 60
    remainder1 = to_index % 60
    if to_index <= 1:
        return to_index
    if remainder1 < remainder:
        remainder1 = (remainder+remainder1)+1
    resultSum = fibo_sum_last_digit(remainder, remainder1)
    return resultSum


def fibo_sum_last_digit(start, end):
    num = [0] * (end + 1)
    num[0] = 0
    num[1] = 1
    for i in range(2, end + 1):
        num[i] = (num[i - 2] + num[i - 1]) % 10
    return sum(num[start:end + 1]) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
