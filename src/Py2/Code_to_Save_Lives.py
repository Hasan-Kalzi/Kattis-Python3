# Code to Save Lives
# Solution by Hasan Kalzi 15-03-2022
# # Link to problem in Kattis: https://open.kattis.com/problems/codetosavelives
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    digit_1 = int("".join(stdin.readline().split()))
    digit_2 = int("".join(stdin.readline().split()))
    sum_digits = str(digit_1 + digit_2)
    for i in range(len(sum_digits)):
        stdout.write(sum_digits[i] + ' ')
    stdout.write('\n')
