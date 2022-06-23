# Bus
# Solution by Hasan Kalzi 26-03-2021
# Link to problem in Kattis https://open.kattis.com/problems/bus
import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = 0
    while k > 0:
        n += 0.5
        n *= 2
        k -= 1
    sys.stdout.write(str(int(n))+'\n')
