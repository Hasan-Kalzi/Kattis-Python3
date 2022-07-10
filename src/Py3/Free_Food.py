# Free Food
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/freefood

# A list contains all days of free food without duplicates
free_food = []
# after range is the inserted number of events of free food: int(input())
for i in range(int(input())):
    start, end = [int(x) for x in input().split()]
    # add all days of free food to the list
    for j in range(start, end + 1):
        if j not in free_food:
            free_food.append(j)
# the list's length is the number of days for free food
if len(free_food) >= 365:
    print(365)
else:
    print(len(free_food))
