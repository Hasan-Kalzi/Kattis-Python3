# Patuljci
# Solution by Hasan Kalzi 07-04-2021
# Link to problem in https://open.kattis.com/problems/patuljci
from sys import stdin, stdout

hat_list = [int(_) for _ in stdin.readlines()]
list_sum = sum(hat_list)
for i in range(9):
    for j in range(i + 1, 9):
        if list_sum - (hat_list[i] + hat_list[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    stdout.write(str(hat_list[k]) + '\n')
            break
