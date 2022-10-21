# Erase Securely
# Solution by Hasan Kalzi 21-10-2022
# Link to problem in Kattis: https://open.kattis.com/problems/erase
from sys import stdin, stdout

n, before, after, succeed = int(stdin.readline()), stdin.readline().strip(), stdin.readline().strip(), 1
if n % 2 == 0:
    for i in range(len(before)):
        if before[i] != after[i]:
            stdout.write("Deletion failed\n")
            succeed = 0
            break
else:
    for i in range(len(before)):
        if before[i] == after[i]:
            stdout.write("Deletion failed\n")
            succeed = 0
            break
if succeed == 1:
    stdout.write("Deletion succeeded\n")