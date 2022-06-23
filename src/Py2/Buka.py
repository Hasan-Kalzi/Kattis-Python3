# Buka
# Solution by Hasan Kalzi 29-03-2021
# Link to problem i https://open.kattis.com/problems/buka
import sys

first_d = int(sys.stdin.readline())
operation = sys.stdin.readline()
second_d = int(sys.stdin.readline())
if operation[0] == '+':
    sys.stdout.write(str(first_d + second_d))
else:
    sys.stdout.write(str(first_d * second_d))
