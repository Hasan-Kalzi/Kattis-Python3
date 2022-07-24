# Seven Wonders
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/sevenwonders
import sys

c, g, t, bounce = 0, 0, 0, 0
played = sys.stdin.readline()
for i in range(len(played) - 1):
    if played[i] == "T":
        t += 1
    elif played[i] == "G":
        g += 1
    elif played[i] == "C":
        c += 1
if t > 0 and g > 0 and c > 0:
    bounce = min(t, c, g) * 7
sys.stdout.write(str((g * g) + (t * t) + (c * c) + bounce))
