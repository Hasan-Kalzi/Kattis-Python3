# Zamka
# Solution by Hasan Kalzi
# https://open.kattis.com/problems/zamka
# Return the minimum and maximum numbers between L and D which the sum of their digits equal
# to the third inserted number X
from sys import stdin, stdout


# return the sum of digits of number n
def sum_number_digits(n):
    sum_number = 0
    while n != 0:
        r = int(n % 10)
        sum_number = sum_number + r
        n = int(n / 10)
    return sum_number


number_l = int(stdin.readline())
number_d = int(stdin.readline())
number_x = int(stdin.readline())
result = []

# Search and calculate every number in the range
for i in range(number_l, number_d + 1):
    if sum_number_digits(i) == number_x:
        result.append(i)
stdout.write(str(result[0])+'\n')
stdout.write(str(result[len(result) - 1])+'\n')
