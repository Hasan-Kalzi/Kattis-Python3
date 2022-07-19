# Odd Gnome
# Solution by Hasan Kalzi 21-03-2021
# Link to problem in https://open.kattis.com/problems/oddgnome
import sys

for _ in range(int(sys.stdin.readline())):
    values = [int(_) for _ in sys.stdin.readline().split()]
    if len(values) == 3:
        sys.stdout.write('2\n')
    else:
        temp = values[1]
        for i in range(2, values[0]):
            if values[i] != temp + 1:
                sys.stdout.write(str(i) + '\n')
                break
            temp = values[i]
