# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    pisano = pisanoPeriod(m)
    remainder = n % pisano
    if n <= 1:
        return n
    last_digit = fibo_last_digit(remainder, m)
    return last_digit


def fibo_last_digit(n, m):
    if n <= 1:
        return n
    num = [0] * (n)
    num[0] = 1
    num[1] = 1
    for i in range(2, n):
        num[i] = (num[i - 1] + num[i - 2]) % m
    return num[n - 1]


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(1, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
