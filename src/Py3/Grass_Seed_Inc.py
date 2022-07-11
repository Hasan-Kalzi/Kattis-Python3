# Grass Seed Inc.
# Solution by Hasan Kalzi 03-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/grassseed

cost_of_one = float(input())
number_of_lawn = int(input())
total_cost = 0
for _ in range(number_of_lawn):
    x, y = input().split()
    total_cost = total_cost + (float(x) * float(y) * cost_of_one)
print("%.7f" % total_cost)
