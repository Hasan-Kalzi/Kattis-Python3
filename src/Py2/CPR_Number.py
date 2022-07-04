# CPR Number
# Solution by Hasan Kalzi 06-12-2021
# Link to problem in Kattis: https://open.kattis.com/problems/cprnummer
from sys import stdin, stdout

personal_number = stdin.readline()
cpr = 0
for i in range(len(personal_number)):
    if i == 0:
        cpr += int(personal_number[0]) * 4
    elif i == 1:
        cpr += int(personal_number[1]) * 3
    elif i == 2:
        cpr += int(personal_number[2]) * 2
    elif i == 3:
        cpr += int(personal_number[3]) * 7
    elif i == 4:
        cpr += int(personal_number[4]) * 6
    elif i == 5:
        cpr += int(personal_number[5]) * 5
    elif i == 7:
        cpr += int(personal_number[7]) * 4
    elif i == 8:
        cpr += int(personal_number[8]) * 3
    elif i == 9:
        cpr += int(personal_number[9]) * 2
    elif i == 10:
        cpr += int(personal_number[10])
if cpr % 11 == 0:
    stdout.write('1')
else:
    stdout.write('0')
