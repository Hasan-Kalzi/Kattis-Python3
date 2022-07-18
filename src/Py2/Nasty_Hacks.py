# Nasty Hacks
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/nastyhacks
from sys import stdin, stdout

# after range is the inserted number of lines: int(input())
for _ in range(int(stdin.readline())):
    r, e, c = map(int, stdin.readline().split())
    if e - r > c:
        stdout.write("advertise\n")
    elif e - r == c:
        stdout.write("does not matter\n")
    else:
        stdout.write("do not advertise\n")
