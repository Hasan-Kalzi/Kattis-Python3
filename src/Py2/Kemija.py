# Kemija
# Solution by Hasan Kalzi 23-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/kemija08
from sys import stdin, stdout

answer = []
j = -1
vocals = ['a', 'e', 'i', 'o', 'u']
# The coded sentence will be given on a single line
coded = stdin.readline()
for i in range(len(coded)):
    if i < j:
        continue
    elif coded[i] in vocals:
        answer.append(coded[i])
        j = i + 3
    else:
        answer.append(coded[i])
stdout.write(''.join(answer))
