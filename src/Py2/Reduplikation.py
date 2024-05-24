# Reduplikation
# Solution by Hasan Kalzi 24-05-2024
# Link to the problem in Kattis: https://open.kattis.com/problems/reduplikation
from sys import stdout, stdin


word = stdin.readline().strip()
for _ in range(int(stdin.readline())):
    stdout.write(word)