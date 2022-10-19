# Mult!
# Solution by Hasan Kalzi 19-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/mult
from sys import stdin, stdout

new_round, base = 1, 0
for _ in range(int(stdin.readline())):
    if new_round == 1:
        base = int(stdin.readline())
        new_round = 0
    else:
        number = int(stdin.readline())
        if number % base == 0:
            stdout.write(str(number) + '\n')
            new_round = 1
