# Laptop Sticker
# Solution by Hasan Kalzi 09-05-2021
# Link to problem in Kattis: https://open.kattis.com/problems/laptopsticker
from sys import stdin, stdout

wc, hc, ws, hs = map(int, stdin.readline().split())
if wc >= ws + 1 and hc > hs + 1:
    stdout.write("1")
else:
    stdout.write("0")
