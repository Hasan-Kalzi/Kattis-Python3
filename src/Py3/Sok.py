# Sok
# Solution by Hasan Kalzi 17-11-2021
# Link to problem in Kattis: https://open.kattis.com/problems/sok
from sys import stdin, stdout

a, b, c = map(int, stdin.readline().split())
i, j, k = map(int, stdin.readline().split())
division_ = (a / i, b / j, c / k)
finish_first = division_.index(min(division_))

if finish_first == 0:
    stdout.write(str(float(0)) + " " + str(float((b - (int(a / i) * j)) - ((a % i) / i) * j)) + " "
                 + str(float((c - (int(a / i) * k)) - ((a % i) / i) * k)))
elif finish_first == 1:
    stdout.write(str(float((a - (int(b / j) * i)) - ((b % j) / j) * i)) + " " + str(float(0)) + " "
                 + str(float((c - (int(b / j) * k)) - ((b % j) / j) * k)))
else:
    stdout.write(str(float((a - (int(c / k) * i)) - ((c % k) / k) * i)) + " "
                 + str(float((b - (int(c / k) * j)) - ((c % k) / k) * j)) + " " + str(float(0)))
