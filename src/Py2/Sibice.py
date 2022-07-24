# Sibice
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/sibice
import math
from sys import stdin, stdout

n, w, h = [int(_) for _ in stdin.readline().split()]
for _ in range(n):
    if int(stdin.readline()) <= math.sqrt((w*w)+(h*h)):
        stdout.write("DA\n")
    else:
        stdout.write("NE\n")
