# Sort Two Numbers
# Solution by Hasan Kalzi 21-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/sorttwonumbers
from sys import stdin, stdout

num_1, num_2 = map(int, stdin.readline().split())
if num_1 >= num_2:
    stdout.write(str(num_2) + " " + str(num_1))
else:
    stdout.write(str(num_1) + " " + str(num_2))
