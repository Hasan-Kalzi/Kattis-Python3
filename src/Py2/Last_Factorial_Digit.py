# Last Factorial Digit
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/lastfactorialdigit
from sys import stdin, stdout
from math import factorial

for _ in range(int(stdin.readline())):
    stdout.write(str(factorial(int(input())) % 10)+'\n')
