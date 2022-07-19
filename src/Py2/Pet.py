# Pet
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/pet
from sys import stdin, stdout

max_grades = 0
winner = 0
for i in range(1, 6):
    player_i = sum([int(_) for _ in stdin.readline().split()])
    if player_i > max_grades:
        max_grades = player_i
        winner = i
stdout.write(str(winner)+' ' + str(max_grades))
