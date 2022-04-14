# Bijele
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/bijele
from sys import stdin, stdout

king, queen, rooks, bishops, knights, pawns = map(int, stdin.readline().split())
stdout.write(str(1 - king) + ' ' + str(1 - queen) + ' ' + str(2 - rooks) + ' ' + str(2 - bishops)
             + ' ' + str(2 - knights) + ' ' + str(8 - pawns))
