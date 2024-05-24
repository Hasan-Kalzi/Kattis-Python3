# Blaðra
# Solution by Hasan Kalzi 24-05-2024
# Link to the problem in Kattis: https://open.kattis.com/problems/bladra2
from sys import stdout, stdin

v, a, t = map(int, stdin.readline().split())
stdout.write(str((v * t) + (0.5 * a * t * t)))
