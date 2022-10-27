# Death Knight Hero
# Solution by Hasan Kalzi 27-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/deathknight
from sys import stdin, stdout

wins = 0
for _ in range(int(stdin.readline())):
    if "CD" not in stdin.readline():
        wins += 1
stdout.write(str(wins))
