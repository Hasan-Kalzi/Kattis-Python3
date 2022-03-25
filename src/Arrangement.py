# Arrangement
# Solution by Hasan Kalzi 11-03-2021
# Link to problem i Kattis: https://open.kattis.com/problems/upprodun
from sys import stdout, stdin

# On the first line is an integer N, and on the second line is an integer M.
n = int(stdin.readline())
m = int(stdin.readline())
complementary = 0
while m % n != 0:
    m -= 1
    complementary += 1

for _ in range(n):
    if complementary > 0:
        stdout.write('*' * int((m / n) + 1) + '\n')
    else:
        stdout.write('*' * int(m / n) + '\n')
    complementary -= 1
