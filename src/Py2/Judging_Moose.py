# Judging Moose
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/judgingmoose
from sys import stdin, stdout

left, right = map(int, stdin.readline().split())
if left == 0 and right == 0:
    stdout.write("Not a moose")
elif left == right:
    stdout.write("Even " + str(left * 2))
else:
    stdout.write("Odd " + str(max(left, right) * 2))
