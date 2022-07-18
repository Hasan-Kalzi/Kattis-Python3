# Missing Numbers
# Solution by Hasan Kalzi 15-01-2021
# Link to problem in Kattis: https://open.   kattis.com/problems/missingnumbers
from sys import stdin, stdout

missing_num = 1
missing = False
for i in range(int(stdin.readline())):
    current = int(stdin.readline())
    while current != missing_num:
        stdout.write(str(missing_num) + '\n')
        missing_num += 1
        if not missing:
            missing = True
    missing_num = current + 1

if not missing:
    stdout.write('good job')
