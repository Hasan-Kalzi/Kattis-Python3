# Sum Squared Digits Function
# Solution by Hasan Kalzi 23-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/sumsquareddigits
from sys import stdin, stdout


def square_digits_base(number, base):
    answer = 0
    while 1 <= number:
        digit = int(number % base)
        answer += digit * digit
        number /= base
    return answer


# after range is the number of data sets that follow: int(input())
for _ in range(int(stdin.readline())):
    i, b, n = [int(_) for _ in stdin.readline().split()]
    n = square_digits_base(n, b)
    stdout.write(str(i) + ' ' + str(n) + '\n')
