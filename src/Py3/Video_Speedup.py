# Video Speedup
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/videospeedup
from sys import stdin, stdout

n, p, k = map(int, stdin.readline().split())
speed_ups = [int(_) for _ in stdin.readline().split()]
speed_ups.append(k)

original = speed_ups[0]
faster = 1
for i in range(len(speed_ups) - 1):
    original += (speed_ups[i + 1] - speed_ups[i]) * ((100 + (faster * p)) / 100)
    faster += 1
stdout.write(str(original))
