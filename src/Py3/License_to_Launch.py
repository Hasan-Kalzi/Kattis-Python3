# License to Launch
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/licensetolaunch

number_of_days = int(input())
junk_values = [int(x) for x in input().split()]
min_junk = min(junk_values)
# find which day has junk equals to the minimum and print it
for i in range(number_of_days):
    if junk_values[i] == min_junk:
        print(i)
        break
