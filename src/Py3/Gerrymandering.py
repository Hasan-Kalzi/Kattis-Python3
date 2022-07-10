# Gerrymandering
# Solution by Hasan Kalzi 25-12-2020
# Link to problem in Kattis: https://open.kattis.com/problems/gerrymandering
import sys

#  The first line contains two integers P and D, where 1≤P≤10000 and 1≤D≤min(1000,P). These indicate, respectively,
#  the number of voting precincts and districts. Following this are P lines describing the precincts.
d, p = [int(_) for _ in sys.intern(sys.stdin.readline()).split()]
values = []
tot_A = 0
tot_wasted_A = 0
tot_B = 0
tot_wasted_B = 0
for _ in range(p + 1):
    values.append([0, 0])
for _ in range(d):
    di, ai, bi = [int(_) for _ in sys.intern(sys.stdin.readline()).split()]
    values[di][0] += ai
    tot_A += ai
    values[di][1] += bi
    tot_B += bi
for district in values[1:]:
    if district[0] > district[1]:
        tot_wasted_A += district[0] - (int((district[0] + district[1]) / 2) + 1)
        tot_wasted_B += district[1]
        sys.stdout.write(
            " ".join(['A', str(district[0] - (int((district[0] + district[1]) / 2) + 1)), str(district[1]), "\n"]))
    else:
        tot_wasted_A += district[0]
        tot_wasted_B += district[1] - (int((district[0] + district[1]) / 2) + 1)
        sys.stdout.write(
            " ".join(['B', str(district[0]), str(district[1] - (int((district[0] + district[1]) / 2) + 1)), "\n"]))

sys.stdout.write(str(abs(tot_wasted_A-tot_wasted_B)/(tot_A+tot_B)))
