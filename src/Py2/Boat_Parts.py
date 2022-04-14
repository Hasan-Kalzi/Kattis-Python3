# Boat Parts
# Solution by Hasan Kalzi 11-03-2021
# Link to the problem in Kattis: https://open.kattis.com/problems/boatparts
import sys

p, n = map(int, sys.stdin.readline().split())

parts_list = []
for i in range(n):
    part = sys.stdin.readline()
    if part not in parts_list:
        parts_list.append(part)
    if len(parts_list) == p:
        sys.stdout.write(str(i + 1))
        break
    elif i == n - 1:
        sys.stdout.write("paradox avoided")
