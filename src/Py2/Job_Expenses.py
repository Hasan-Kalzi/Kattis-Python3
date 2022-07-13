# Job Expenses
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/jobexpenses
from sys import stdin, stdout

stdin.readline()
values = [int(_) for _ in stdin.readline().split() if int(_) < 0]
stdout.write(str(sum(values)*-1))
