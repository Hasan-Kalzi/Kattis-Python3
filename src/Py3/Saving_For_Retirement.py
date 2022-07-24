# Saving For Retirement
# Solution by Hasan Kalzi 05-04-2021
# Link to problem in https://open.kattis.com/problems/acm
from sys import stdin, stdout

b, b_r, b_s, a, a_s = map(int, stdin.readline().split())
bob = (b_r - b) * b_s
a_r = int(bob / a_s)
if a_r * a_s <= bob:
    a_r += 1
stdout.write(str(a + a_r)+'\n')
