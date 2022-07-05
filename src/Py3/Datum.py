# Datum
# Solution by Hasan Kalzi 22-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/datum
from datetime import date

day, month = [int(x) for x in input().split()]
weekdays_2009 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date = date(2009, month, day)
print(weekdays_2009[date.weekday()])
