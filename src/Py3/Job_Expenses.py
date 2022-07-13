# Job Expenses
# Solution by Hasan Kalzi 21-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/jobexpenses

input()
values = sorted([int(x) for x in input().split()])
expenses = 0
for i in values:
    if i < 0:
        expenses += abs(i)
    else:
        break
print(expenses)
