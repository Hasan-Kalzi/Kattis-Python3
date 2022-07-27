# Spavanac
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/spavanac
from sys import stdin, stdout

hour, minutes = map(int, stdin.readline().split())  # [Hour,minutes]
# in case the minutes less than 45 the hour scorpion will go back one and calculate the minutes
if minutes - 45 < 0:
    hour -= 1  # decrease hour by 1
    minutes = 60 + minutes - 45
# in case the minutes over or equals 45
else:
    minutes = minutes - 45

# in case the hour got negative
if hour < 0:
    hour = 23
# print the time before 45 minutes of the inserted time
stdout.write(str(hour) + ' ' + str(minutes))
