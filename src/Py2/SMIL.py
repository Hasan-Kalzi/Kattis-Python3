# SMIL
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/smil
from sys import stdin, stdout

smil = stdin.readline().strip()
for i in range(len(smil)):
    if smil[i] == ':' or smil[i] == ';':
        if i + 1 != len(smil):
            if smil[i + 1] == ')':
                stdout.write(str(i) + '\n')
                i = i + 1
            elif smil[i + 1] == '-':
                if i + 2 != len(smil):
                    if smil[i + 2] == ')':
                        stdout.write(str(i) + '\n')
                        i = i + 2
