# The Easiest Problem Is This One
# Solution by Hasan Kalzi 11-03-2021
# Link to problem in https://open.kattis.com/problems/easiest
import sys

while True:
    number = int(sys.stdin.readline())
    if number == 0:
        break
    sum_of_digits = sum(int(_) for _ in str(number))
    i = 11
    while True:
        if sum(int(_) for _ in str(number * i)) == sum_of_digits:
            sys.stdout.write(str(i) + '\n')
            break
        i += 1

