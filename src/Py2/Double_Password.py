# Double Password
# Solution by Hasan Kalzi 14-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/doublepassword
from sys import stdin, stdout

code_1, code_2, miss = stdin.readline().strip(), stdin.readline().strip(), 4
for i in range(4):
    if code_1[i] == code_2[i]:
        miss -= 1
print(2**miss)
