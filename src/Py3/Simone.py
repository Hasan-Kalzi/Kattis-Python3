# Simone
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/simone
from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
colours = [0] * k
lights = stdin.readline().split()
for light in lights:
    colours[int(light) - 1] += 1
min_rep, reps, answer = min(colours), 0, []
if colours.count(min_rep) > 1:
    for i in range(colours.index(min_rep), k):
        if colours[i] == min_rep:
            reps += 1
            answer.append(i + 1)
        if min_rep not in colours[i:k]:
            break
    stdout.write(str(reps) + '\n')
    stdout.write(" ".join(str(_) for _ in answer))
else:
    stdout.write('1\n')
    stdout.write(str(colours.index(min_rep) + 1))
