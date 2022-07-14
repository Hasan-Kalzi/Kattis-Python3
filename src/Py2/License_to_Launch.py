# License to Launch
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/licensetolaunch
from sys import stdin, stdout
number_of_days = int(stdin.readline())
junk_values = [int(_) for _ in stdin.readline().split()]
# find which day has junk equals to the minimum and print it
stdout.write(str(junk_values.index(min(junk_values))))

