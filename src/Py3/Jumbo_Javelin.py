# Jumbo Javelin
# Solution by Hasan Kalzi 03-04-2021
# Link to problem in https://open.kattis.com/problems/jumbojavelin

from sys import stdin, stdout
values = list(map(int, stdin.readlines()))
stdout.write(str(sum(values[1:]) - values[0] + 1))
