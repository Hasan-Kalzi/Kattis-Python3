# Knight Packing
# Solution by Hasan Kalzi 28-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/knightpacking
from sys import stdout, stdin

if int(stdin.readline()) % 2 == 0:
    stdout.write("second")
else:
    stdout.write("first")
