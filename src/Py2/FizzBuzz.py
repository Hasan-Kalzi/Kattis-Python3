# FizzBuzz
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/fizzbuzz
from sys import stdin, stdout

x, y, n = map(int, stdin.readline().split())
for i in range(1, n + 1):
    if i % x == 0 and i % y == 0:
        stdout.write("FizzBuzz\n")
    elif i % x == 0:
        stdout.write("Fizz\n")
    elif i % y == 0:
        stdout.write("Buzz\n")
    else:
        stdout.write(str(i) + '\n')
