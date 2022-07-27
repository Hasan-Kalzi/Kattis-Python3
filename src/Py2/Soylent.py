# Soylent
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/soylent
import sys

for _ in range(int(sys.stdin.readline())):
    i = 0
    calories = int(sys.stdin.readline())
    while i * 400 < calories:
        i += 1
    sys.stdout.write(str(i)+'\n')
