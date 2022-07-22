# Railroad
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/railroad2

x_shaped, y_shaped = input().split()
# the Y shaped must be an even number
if int(y_shaped) % 2 == 0:
    print("possible")
else:
    print("impossible")
