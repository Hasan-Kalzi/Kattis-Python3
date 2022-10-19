# Divvying Up
# Solution by Hasan Kalzi 19-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/divvyingup
from sys import stdin, stdout

stdin.readline()
if sum([int(_) for _ in stdin.readline().split()]) % 3 == 0:
    stdout.write("Yes")
else:
    stdout.write("no")
