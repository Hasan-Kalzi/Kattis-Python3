# Gene Block
# Solution by Hasan Kalzi 16-08-2022
# Link to problem in Kattis: https://open.kattis.com/problems/geneblock
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    num = stdin.readline().strip()
    i = int(num)
    if i < 7:
        stdout.write('-1\n')
    elif num[-1] == '7' and i > 0:
        stdout.write('1\n')
    elif num[-1] == '4' and i >= 14:
        stdout.write('2\n')
    elif num[-1] == '1' and i >= 21:
        stdout.write('3\n')
    elif num[-1] == '8' and i >= 28:
        stdout.write('4\n')
    elif num[-1] == '5' and i >= 35:
        stdout.write('5\n')
    elif num[-1] == '2' and i >= 42:
        stdout.write('6\n')
    elif num[-1] == '9' and i >= 49:
        stdout.write('7\n')
    elif num[-1] == '6' and i >= 56:
        stdout.write('8\n')
    elif num[-1] == '3' and i >= 63:
        stdout.write('9\n')
    elif num[-1] == '0' and i >= 70:
        stdout.write('10\n')
    else:
        stdout.write('-1\n')
