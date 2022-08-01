# Transit Woes
# Solution by Hasan Kalzi 10-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/transitwoes
import sys

leaving_time, arriving_time, number_of_buses = [int(_) for _ in sys.stdin.readline().split()]
walking_periods = [int(_) for _ in sys.stdin.readline().split()]
riding_periods = [int(_) for _ in sys.stdin.readline().split()]
arriving_times = [int(_) for _ in sys.stdin.readline().split()]
consumed_time = walking_periods[0] + leaving_time
for i in range(number_of_buses):
    consumed_time += arriving_times[i] - consumed_time
    consumed_time += riding_periods[i]
    consumed_time += walking_periods[i + 1]
if consumed_time > arriving_time:
    sys.stdout.write("no")
else:
    sys.stdout.write("yes")
