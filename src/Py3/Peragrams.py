# Peragrams
# Solution by Hasan Kalzi 19-07-2022
# Link to problem in Kattis: https://open.kattis.com/problems/peragrams
from sys import stdin, stdout

x, i = -1, 0
word = sorted(stdin.readline().strip())
while i < len(word):
    if word[i] not in word[i + 1:]:
        x += 1
        i += 1
    else:
        i += 2
if x == - 1:
    x = 0
stdout.write(str(x))
