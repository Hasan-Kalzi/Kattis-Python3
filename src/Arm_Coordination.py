# Arm Coordination
# Solution by Hasan Kalzi 06-12-2021
# Link to problem i Kattis: https://open.kattis.com/problems/armcoordination
from sys import stdin, stdout

x, y = map(int, stdin.readline().split())
r = int(stdin.readline())
stdout.write(str(x + r) + " " + str(y + r) + "\n" + str(x + r) + " " + str(y - r) + "\n" +
             str(x - r) + " " + str(y - r) + "\n" + str(x - r) + " " + str(y + r) + "\n")
