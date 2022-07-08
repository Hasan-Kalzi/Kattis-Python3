# Finding An A
# Solution by Hasan Kalzi: 14-02-2022
# Link to the problem: https://open.kattis.com/problems/findingana
from sys import stdin, stdout

word = stdin.readline()
for i in range(len(word)):
    if word[i] == 'a':
        stdout.write(word[i:])
        break
