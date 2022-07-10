# Free Food
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/freefood
from sys import stdin, stdout

# A list contains all days of free food without duplicates
free_food = []
# after range is the inserted number of events of free food: int(input())
for i in range(int(stdin.readline())):
    start, end = map(int, stdin.readline().split())
    # add all days of free food to the list
    for j in range(start, end + 1):
        if j not in free_food:
            free_food.append(j)
# the list's length is the number of days for free food
if len(free_food) >= 365:
    stdout.write('365')
else:
    stdout.write(str(len(free_food)))
