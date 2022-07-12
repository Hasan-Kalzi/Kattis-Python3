# Inquiry I
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/inquiryi
from sys import stdin, stdout

n = int(stdin.readline())

values = [0]*n
not_sq_sum = 0
for i in range(n):
    value = int(stdin.readline())
    values[i] = value
    not_sq_sum += value
sum_sq = 0
for i in range(n - 1):
    not_sq_sum -= values[i]
    sum_sq += values[i] ** 2
    values[i] = sum_sq * not_sq_sum

stdout.write(str(max(values)))
