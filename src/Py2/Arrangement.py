# Arrangement
# Solution by Hasan Kalzi 11-03-2021
# Link to problem i Kattis: https://open.kattis.com/problems/upprodun
import sys

# On the first line is an integer N, and on the second line is an integer M.
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
complementary = 0
while m % n != 0:
    m -= 1
    complementary += 1

for _ in range(n):
    if complementary > 0:
        sys.stdout.write('*' * int((m / n) + 1) + '\n')
    else:
        sys.stdout.write('*' * int(m / n) + '\n')
    complementary -= 1
