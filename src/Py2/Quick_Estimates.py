# Quick Estimates
# Solution by Hasan Kalzi 23-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/quickestimate
from sys import stdin, stdout
# after range is the inserted number of numbers: int(input())
for _ in range(int(stdin.readline())):
    stdout.write(str(len(stdin.readline().strip()))+'\n')
