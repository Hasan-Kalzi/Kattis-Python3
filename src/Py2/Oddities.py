# Oddities
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/oddities
from sys import stdin, stdout

# after range is the inserted number of tests: int(input())
for _ in range(int(stdin.readline())):
    number = int(stdin.readline())
    if number % 2 == 0:
        stdout.write(str(number) + " is even\n")
    else:
        stdout.write(str(number) + " is odd\n")
