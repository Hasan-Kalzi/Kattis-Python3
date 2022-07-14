# coding=utf-8
# Lost Lineup
# Solution by Hasan Kalzi 21-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/lostlineup
from sys import stdin, stdout

# The first line contains a single integer n (1≤n≤100), the number of people in the line.
n = int(stdin.readline())

# Print a single line with n integers, the people in the order of the original lineup.
# It is guaranteed that there is always a unique solution.
people = [1] * n

# The second line contains n−1 space separated integers,
# where di (0≤di≤n−2) is the number of people between the (i+1)th person and Jimmy.
values = [int(_) for _ in stdin.readline().split()]

# after range is the inserted number of people n: int(sys.stdin.readline())
for i in range(n-1):
    people[values[i]+1] = i + 2
for element in people:
    stdout.write(str(element)+" ")
