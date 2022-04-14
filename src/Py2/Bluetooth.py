# Bluetooth
# Solution by Hasan Kalzi 06-11-2021
# Link to problem in Kattis: https://open.kattis.com/problems/bluetooth
from sys import stdin, stdout

left_down = [0, 0, 0, 0, 0, 0, 0, 0]
left_up = [0, 0, 0, 0, 0, 0, 0, 0]
right_down = [0, 0, 0, 0, 0, 0, 0, 0]
right_up = [0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(int(stdin.readline())):
    tooth = stdin.readline()
    if tooth[0] == '-':
        if tooth[3] == 'm':
            left_down[int(tooth[1]) - 1] = 1
        else:
            left_down[int(tooth[1]) - 1] = 2
    elif tooth[0] == '+':
        if tooth[3] == 'm':
            left_up[int(tooth[1]) - 1] = 1
        else:
            left_up[int(tooth[1]) - 1] = 2
    elif tooth[1] == '-':
        if tooth[3] == 'm':
            right_down[int(tooth[0]) - 1] = 1
        else:
            right_down[int(tooth[0]) - 1] = 2
    elif tooth[1] == '+':
        if tooth[3] == 'm':
            right_up[int(tooth[0]) - 1] = 1
        else:
            right_up[int(tooth[0]) - 1] = 2
if 2 in left_up or 2 in left_down:
    if 2 in right_up or 2 in right_down:
        stdout.write('2')
    elif 0 in right_down and 0 in right_up:
        stdout.write('1')
    else:
        stdout.write('2')

elif 2 in right_up or 2 in right_down:
    if 2 in left_up or 2 in left_down:
        stdout.write('2')
    elif 0 in left_up and 0 in left_down:
        stdout.write('0')
    else:
        stdout.write('2')

else:
    if 0 in left_up and 0 in left_down:
        stdout.write('0')
    elif 0 in right_down and 0 in right_up:
        stdout.write('1')
    else:
        stdout.write('2')
