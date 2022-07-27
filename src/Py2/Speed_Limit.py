# coding=utf-8
# Speed Limit
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/speedlimit
from sys import stdin, stdout

while 1:
    number_data_sets = int(stdin.readline())
    driving_times = [0]  # a list to save all times in the set
    driving_miles = 0
    #  A value of −1 for n signals the end of the input.
    if number_data_sets == -1:
        break
    for i in range(number_data_sets):
        values = stdin.readline().split()
        driving_times.append(int(values[1]))
        driving_miles += int(values[0]) * (int(values[1]) - driving_times[i])
    stdout.write(str(driving_miles) + " miles\n")
