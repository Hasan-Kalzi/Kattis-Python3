# Tower Construction
# Solution by Hasan Kalzi 16-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/tornbygge/en
from sys import stdin, stdout

stdin.readline()
towers = 0
prev = 0
for block in stdin.readline().split():
    if prev < int(block):
        towers += 1
    prev = int(block)
stdout.write(str(towers))
