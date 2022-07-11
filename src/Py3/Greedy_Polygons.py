# Greedy Polygons
# Solution by Hasan Kalzi 03-04-2021
# Link to problem in https://open.kattis.com/problems/greedypolygons
from sys import stdin, stdout
from math import pi, tan

for _ in range(int(stdin.readline())):
    num_sides, initial_size, expansion_size, num_expansions = map(int, stdin.readline().split())
    stdout.write(str((0.25 * num_sides * initial_size * initial_size * (1 / tan(pi / num_sides)))
                     + (pi * expansion_size * num_expansions * expansion_size * num_expansions)
                     + num_sides * (expansion_size * num_expansions * initial_size))+'\n')
