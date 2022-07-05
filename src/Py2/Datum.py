# Datum
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/datum
from sys import stdin, stdout
from datetime import date

day, month = map(int, stdin.readline().split())
weekdays_2009 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date = date(2009, month, day)
stdout.write(weekdays_2009[date.weekday()])
