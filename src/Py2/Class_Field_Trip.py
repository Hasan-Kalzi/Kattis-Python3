# Class Field Trip
# Solution by Hasan Kalzi 05-04-2023
# Link to problem in Kattis: https://open.kattis.com/problems/classfieldtrip
from sys import stdout, stdin
answer = sorted(stdin.readline().strip()+stdin.readline().strip())
for letter in answer:
    stdout.write(letter)