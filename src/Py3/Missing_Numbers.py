# Missing Numbers
# Solution by Hasan Kalzi 15-01-2021
# Link to problem in Kattis: https://open.kattis.com/problems/missingnumbers
import sys

missing_num = 1
missing = False
for i in range(int(sys.stdin.readline())):
    current = int(sys.stdin.readline())
    while current != missing_num:
        sys.stdout.write(str(missing_num) + '\n')
        missing_num += 1
        if not missing:
            missing = True
    missing_num = current + 1

if not missing:
    sys.stdout.write('good job')
