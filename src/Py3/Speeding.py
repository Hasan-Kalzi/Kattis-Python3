# Speeding
# Solution by Hasan Kalzi 11-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/speeding
import sys

maxSpeed = 0
n = int(sys.stdin.readline())  # number of photographs
time1, distance1 = map(int, sys.stdin.readline().split())
for _ in range(n-1):
    time2, distance2 = map(int, sys.stdin.readline().split())
    avrSpeed = (distance2 - distance1) / (time2 - time1)
    if avrSpeed > maxSpeed:
        maxSpeed = avrSpeed
    time1, distance1 = time2, distance2
sys.stdout.write(str(int(maxSpeed)))
