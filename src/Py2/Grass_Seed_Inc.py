# Grass Seed Inc.
# Solution by Hasan Kalzi 03-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/grassseed
from sys import stdin, stdout
cost_of_one = float(stdin.readline())
number_of_lawn = int(stdin.readline())
total_cost = 0
for _ in range(number_of_lawn):
    x, y = map(float, stdin.readline().split())
    total_cost = total_cost + (x * y * cost_of_one)
stdout.write("%.7f" % total_cost)
