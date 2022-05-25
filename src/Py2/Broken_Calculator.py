# Broken Calculator
# Solution by Hasan Kalzi 15-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/brokencalculator
from sys import stdin, stdout

result = 1
for _ in range(int(stdin.readline())):
    a, o, b = stdin.readline().strip().split()
    if o == '+':
        result = (int(a) + int(b)) - result
    elif o == '-':
        result = result * (int(a) - int(b))
    elif o == '*':
        result = (int(a) * int(b)) * (int(a) * int(b))
    else:
        if int(a) % 2 == 0:
            result = int(int(a) / 2)
        else:
            result = int((int(a)+1)/2)
    stdout.write(str(result) + '\n')
