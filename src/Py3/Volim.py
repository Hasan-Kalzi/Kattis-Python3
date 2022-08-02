# Arm Coordination
# Solution by Hasan Kalzi 06-12-2021
# Link to problem in Kattis: https://open.kattis.com/problems/volim
from sys import stdin, stdout

player = int(stdin.readline())
total_time = 0
for _ in range(int(stdin.readline())):
    time, answer = stdin.readline().split()
    total_time += int(time)
    if total_time >= 210:
        stdout.write(str(player))
        break
    if answer == 'T':
        player += 1
        if player == 9:
            player = 1
