# Railroad
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/railroad2
from sys import stdin, stdout
x_shaped, y_shaped = stdin.readline().strip().split()
# the Y shaped must be an even number
if int(y_shaped) % 2 == 0:
    stdout.write("possible")
else:
    stdout.write("impossible")
