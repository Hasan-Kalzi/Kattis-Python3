# A New Alphabet
# Solution by Hasan Kalzi 07-04-2021
# Link to problem in https://open.kattis.com/problems/anewalphabet
from sys import stdin, stdout

for char in stdin.readline():
    ascii_char = ord(char)
    if ascii_char == 65 or ascii_char == 97:
        stdout.write('@')
    elif ascii_char == 66 or ascii_char == 98:
        stdout.write('8')
    elif ascii_char == 67 or ascii_char == 99:
        stdout.write('(')
    elif ascii_char == 68 or ascii_char == 100:
        stdout.write('|)')
    elif ascii_char == 69 or ascii_char == 101:
        stdout.write('3')
    elif ascii_char == 70 or ascii_char == 102:
        stdout.write('#')
    elif ascii_char == 71 or ascii_char == 103:
        stdout.write('6')
    elif ascii_char == 72 or ascii_char == 104:
        stdout.write('[-]')
    elif ascii_char == 73 or ascii_char == 105:
        stdout.write('|')
    elif ascii_char == 74 or ascii_char == 106:
        stdout.write('_|')
    elif ascii_char == 75 or ascii_char == 107:
        stdout.write('|<')
    elif ascii_char == 76 or ascii_char == 108:
        stdout.write('1')
    elif ascii_char == 77 or ascii_char == 109:
        stdout.write('[]\/[]')
    elif ascii_char == 78 or ascii_char == 110:
        stdout.write('[]\[]')
    elif ascii_char == 79 or ascii_char == 111:
        stdout.write('0')
    elif ascii_char == 80 or ascii_char == 112:
        stdout.write('|D')
    elif ascii_char == 81 or ascii_char == 113:
        stdout.write('(,)')
    elif ascii_char == 82 or ascii_char == 114:
        stdout.write('|Z')
    elif ascii_char == 83 or ascii_char == 115:
        stdout.write('$')
    elif ascii_char == 84 or ascii_char == 116:
        stdout.write('\'][\'')
    elif ascii_char == 85 or ascii_char == 117:
        stdout.write('|_|')
    elif ascii_char == 86 or ascii_char == 118:
        stdout.write('\\/')
    elif ascii_char == 87 or ascii_char == 119:
        stdout.write('\\/\\/')
    elif ascii_char == 88 or ascii_char == 120:
        stdout.write('}{')
    elif ascii_char == 89 or ascii_char == 121:
        stdout.write('`/')
    elif ascii_char == 90 or ascii_char == 122:
        stdout.write('2')
    else:
        stdout.write(char)
