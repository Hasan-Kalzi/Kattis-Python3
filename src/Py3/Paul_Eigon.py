# Paul Eigon
# Solution by Hasan Kalzi 06-04-2021
# Link to problem in https://open.kattis.com/problems/pauleigon
from sys import stdin, stdout

n, p, o = map(int, stdin.readline().split())
if int((p + o) / n) % 2 == 0:
    stdout.write("paul")
else:
    stdout.write("opponent")
