# N-sum
# Solution by Hasan Kalzi 31-10-2021
# Link to problem in Kattis: https://open.kattis.com/problems/nsum
from sys import stdin, stdout
stdin.readline()
stdout.write(str(sum(map(int, stdin.readline().split()))))
