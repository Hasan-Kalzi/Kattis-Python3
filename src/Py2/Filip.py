# Filip
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/filip
from sys import stdin, stdout


def reverse_number(n):
    reversed_number = 0
    while n != 0:
        r = int(n % 10)
        reversed_number = reversed_number * 10 + r
        n = int(n / 10)
    return reversed_number


x_, y_ = map(int, stdin.readline().split())
x = reverse_number(x_)
y = reverse_number(y_)
if x > y:
    stdout.write(str(x))
else:
    stdout.write(str(y))
