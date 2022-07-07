# Faktor
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/faktor
from sys import stdin, stdout
import math

a, i = map(int, stdin.readline().split())
stdout.write(str(int(math.ceil(a * (i - 1 + 0.00000000001)))))
