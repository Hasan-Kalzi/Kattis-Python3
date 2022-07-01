# Cooking Water
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/cookingwater
from sys import stdin, stdout

max_s, min_e = 0, 10000
gunilla = 0
for _ in range(int(stdin.readline())):
    s, e = map(int, stdin.readline().split())
    if s > max_s:
        max_s = s
    if e < min_e:
        min_e = e
    if max_s > min_e:
        stdout.write("edward is right")
        gunilla = 1
        break
if gunilla == 0:
    stdout.write("gunilla has a point")
