# Hot Springs
# Solution by Hasan Kalzi 15-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/hotsprings
from sys import stdin, stdout

n = int(stdin.readline())
num_list = [int(_) for _ in stdin.readline().split()]
num_list.sort()
if n % 2 == 0:
    for i in range(int(n / 2) - 1, -1, -1):
        stdout.write(str(num_list[n - i - 1]) + ' ' + str(num_list[i]) + ' ')
else:
    for i in range(int(n / 2), -1, -1):
        if i != int(n / 2):
            stdout.write(str(num_list[n - i - 1]) + ' ' + str(num_list[i]) + ' ')
        else:
            stdout.write(str(num_list[i]) + ' ')
