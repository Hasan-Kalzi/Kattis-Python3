# Identifying Map Tiles
# Solution by Hasan Kalzi 23-03-2021
# Link to problem in https://open.kattis.com/problems/maptiles2
import sys

coordinate = sys.stdin.readline()

x = 0
y = 0
k = 0
for i in range(len(coordinate) - 1):
    k = pow(2, len(coordinate) - i - 2)
    if coordinate[i] == '1':
        x += k
    elif coordinate[i] == '2':
        y += k
    elif coordinate[i] == '3':
        x += k
        y += k

sys.stdout.write(str(len(coordinate) - 1) + ' ' + str(x) + ' ' + str(y))
