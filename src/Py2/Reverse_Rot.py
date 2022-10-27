# Reverse Rot
# Solution by Hasan Kalzi 06-03-2022
# Link to problem in Kattis: https://open.kattis.com/problems/reverserot
from sys import stdin, stdout

letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', '_', '.')

while 1:
    line = stdin.readline().strip()
    if line == '0':
        break
    rotation, msg_code = line.split()
    rotation = int(rotation)
    for i in range(len(msg_code) - 1, -1, -1):
        stdout.write(letters[(letters.index(msg_code[i]) + rotation) % 28])
    stdout.write('\n')
