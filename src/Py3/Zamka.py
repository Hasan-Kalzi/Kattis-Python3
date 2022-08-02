# Zamka
# Solution by Hasan Kalzi
# https://open.kattis.com/problems/zamka
# Return the minimum and maximum numbers between L and D which the sum of their digits equal
# to the third inserted number X


# return the sum of digits of number n
def sum_number_digits(n):
    sum_number = 0
    while n != 0:
        r = int(n % 10)
        sum_number = sum_number + r
        n = int(n / 10)
    return sum_number


number_l = int(input())
number_d = int(input())
number_x = int(input())
result = []

# Search and calculate every number in the range
for i in range(number_l, number_d +1):
    if sum_number_digits(i) == number_x:
        result.append(i)
print(result[0])
print(result[len(result)-1])
