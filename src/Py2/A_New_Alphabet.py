# A New Alphabet
# Solution by Hasan Kalzi 07-04-2021
# Link to problem i https://open.kattis.com/problems/anewalphabet
from sys import stdin, stdout
for char in stdin.readline():
    ascii= ord(char)
    if ascii == 65 or ascii == 97:
        stdout.write('@')
    elif ascii == 66 or ascii == 98:
        stdout.write('8')
    elif ascii == 67 or ascii == 99:
        stdout.write('(')
    elif ascii == 68 or ascii == 100:
        stdout.write('|)')
    elif ascii == 69 or ascii == 101:
        stdout.write('3')
    elif ascii == 70 or ascii == 102:
        stdout.write('#')
    elif ascii == 71 or ascii == 103:
        stdout.write('6')
    elif ascii == 72 or ascii == 104:
        stdout.write('[-]')
    elif ascii == 73 or ascii == 105:
        stdout.write('|')
    elif ascii == 74 or ascii == 106:
        stdout.write('_|')
    elif ascii == 75 or ascii == 107:
        stdout.write('|<')
    elif ascii == 76 or ascii == 108:
        stdout.write('1')
    elif ascii == 77 or ascii == 109:
        stdout.write('[]\/[]')
    elif ascii == 78 or ascii == 110:
        stdout.write('[]\[]')
    elif ascii == 79 or ascii == 111:
        stdout.write('0')
    elif ascii == 80 or ascii == 112:
        stdout.write('|D')
    elif ascii == 81 or ascii == 113:
        stdout.write('(,)')
    elif ascii == 82 or ascii == 114:
        stdout.write('|Z')
    elif ascii == 83 or ascii == 115:
        stdout.write('$')
    elif ascii == 84 or ascii == 116:
        stdout.write('\'][\'')
    elif ascii == 85 or ascii == 117:
        stdout.write('|_|')
    elif ascii == 86 or ascii == 118:
        stdout.write('\\/')
    elif ascii == 87 or ascii == 119:
        stdout.write('\\/\\/')
    elif ascii == 88 or ascii == 120:
        stdout.write('}{')
    elif ascii == 89 or ascii == 121:
        stdout.write('`/')
    elif ascii == 90 or ascii == 122:
        stdout.write('2')
    else:
        stdout.write(char)















