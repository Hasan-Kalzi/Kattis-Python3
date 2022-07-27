# Stand on Zanzibar
# Solution by Hasan Kalzi 25-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/zanzibar
from sys import stdin, stdout
# after range is the inserted number of cases: int(input())
for _ in range(int(stdin.readline())):
    # the lower bound for the number of turtles not born on Zanzibar.
    lower_bound = 0
    values = [int(_) for _ in stdin.readline().split()]
    for i in range(len(values)):
        if values[i] == 0:
            break
        if values[i + 1] > values[i] * 2:
            lower_bound += values[i + 1] - (2 * values[i])
    stdout.write(str(lower_bound)+'\n')
