# Bijele
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/bijele

king, queen, rooks, bishops, knights, pawns = [int(x) for x in input().split()]
print(1 - king, 1 - queen, 2 - rooks, 2 - bishops, 2 - knights, 8 - pawns)
