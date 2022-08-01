# Ultimate Binary Watch
# Solution by Hasan Kalzi 06-12-2021
# Link to problem in Kattis: https://open.kattis.com/problems/ultimatebinarywatch
from sys import stdin, stdout

position_0 = ['.', '.', '.', '.', '.', '.', '.', '.', '*', '*']
position_1 = ['.', '.', '.', '.', '*', '*', '*', '*', '.', '.']
position_2 = ['.', '.', '*', '*', '.', '.', '*', '*', '.', '.']
position_3 = ['.', '*', '.', '*', '.', '*', '.', '*', '.', '*']

time_now = stdin.readline().strip()[:]
bin_clock = ""
for i in range(4):
    if i == 0:
        bin_clock += position_0[int(time_now[0])] + ' ' + \
                     position_0[int(time_now[1])] + '   ' + \
                     position_0[int(time_now[2])] + ' ' + \
                     position_0[int(time_now[3])] + '\n'
    elif i == 1:
        bin_clock += position_1[int(time_now[0])] + ' ' + \
                     position_1[int(time_now[1])] + '   ' + \
                     position_1[int(time_now[2])] + ' ' + \
                     position_1[int(time_now[3])] + '\n'
    elif i == 2:
        bin_clock += position_2[int(time_now[0])] + ' ' + \
                     position_2[int(time_now[1])] + '   ' + \
                     position_2[int(time_now[2])] + ' ' + \
                     position_2[int(time_now[3])] + '\n'
    else:
        bin_clock += position_3[int(time_now[0])] + ' ' + \
                     position_3[int(time_now[1])] + '   ' + \
                     position_3[int(time_now[2])] + ' ' + \
                     position_3[int(time_now[3])] + '\n'
stdout.write(bin_clock)
