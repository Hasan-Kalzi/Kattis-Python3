# Piece of Cake!
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/pieceofcake2
from sys import stdin, stdout

n, h, v = map(int, stdin.readline().split())
volume = 0
if h >= n - h:
    volume = h * 4
else:
    volume = (n - h) * 4
if v >= n - v:
    volume = volume * v
else:
    volume = (n - v) * volume
stdout.write(str(volume))
