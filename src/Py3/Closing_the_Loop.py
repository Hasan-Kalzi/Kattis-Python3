# Closing the Loop
# Solution by Hasan Kalzi 26-03-2021
# Link to problem in https://open.kattis.com/problems/closingtheloop
import sys

for i in range(int(sys.stdin.readline())):
    loop = 0
    red, blue = [], []
    sys.stdin.readline()
    value = sys.stdin.readline().split()
    for v in value:
        if 'B' in v:
            blue.append(int(v[0:len(v) - 1].replace('B', '')))
        else:
            red.append(int(v[0:len(v) - 1].replace('R', '')))
    blue = sorted(blue, reverse=True)
    red = sorted(red, reverse=True)
    for j in range(min(len(blue), len(red))):
        loop += blue[j] + red[j] - 2
    sys.stdout.write("Case #" + str(i+1) + ': ' + str(loop) + '\n')
