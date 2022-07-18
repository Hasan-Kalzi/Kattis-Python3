# No Duplicates
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/nodup
from sys import stdin, stdout
values = stdin.readline().split()
x = 0
while x <= len(values) - 1:
    if values[x] in values[x + 1:]:
        stdout.write("no\n")
        break
    if x == len(values) - 1:
        stdout.write("yes\n")
    x += 1
