# 99 Problems
# Solution by Hasan Kalzi 17-05-2022
# Link to problem in https://open.kattis.com/problems/99problems
from sys import stdin, stdout

number = stdin.readline().strip()
if 1 <= len(number) <= 2:
    stdout.write("99")
elif number[-1] == '9' and number[-2] == '9':
    stdout.write(number)
else:
    bigger = int(number[:-2] + '99')
    smaller = int(str(int(number[:-2]) - 1) + '99')
    if bigger - int(number) <= int(number) - smaller:
        stdout.write(str(bigger))
    else:
        stdout.write(str(smaller))
