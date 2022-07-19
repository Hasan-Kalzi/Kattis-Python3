# Odd Echo
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/oddecho
from sys import stdin, stdout

for i in range(1, int(stdin.readline()) + 1):
    if i % 2 != 0:
        stdout.write(stdin.readline())
    else:
        stdin.readline()
