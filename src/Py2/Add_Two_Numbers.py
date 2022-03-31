# Add Two Numbers
# Solution by Hasan Kalzi 21-06-2021
# # Link to problem in Kattis6: https://open.kattis.com/problems/addtwonumbers
from sys import stdin, stdout

stdout.write(str(sum(map(int, stdin.readline().split()))))
