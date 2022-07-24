# Simone
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/simone
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
colours = [0] * k
lights = [int(_) for _ in stdin.readline().split()]
for light in lights:
    colours[light - 1] += 1
min_rep = min(colours)
answer = []
reps = 0
for i in range(k):
    if colours[i] == min_rep:
        reps += 1
        answer.append(i + 1)
stdout.write(str(reps) + '\n')
stdout.write(" ".join(str(x) for x in answer))
