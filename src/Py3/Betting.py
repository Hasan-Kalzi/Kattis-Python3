# Betting
# Solution by Hasan Kalzi 14-03-2022
# Link to the problem in Kattis: https://open.kattis.com/problems/betting
from sys import stdin, stdout

percentage = int(stdin.readline())
stdout.write(str((1/percentage)*100)+'\n'+str((1/(100-percentage))*100))
