# Bela
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/bela
from sys import stdin, stdout

n, b = stdin.readline().strip().split(" ")
score = 0
for _ in range(int(n) * 4):
    values = stdin.readline().strip()
    if values[0] == "A":
        score += 11
    elif values[0] == "K":
        score += 4
    elif values[0] == "Q":
        score += 3
    elif values[0] == "J":
        if values[1] == b:
            score += 20
        else:
            score += 2
    elif values[0] == "T":
        score += 10
    elif values[0] == "9":
        if values[1] == b:
            score += 14
stdout.write(str(score))
