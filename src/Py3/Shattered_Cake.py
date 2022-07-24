# Shattered Cake
# Solution by Hasan Kalzi 25-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/shatteredcake

sum_area = 0
w = int(input())
# after range is the inserted number of pieces: int(input())
for _ in range(int(input())):
    # the width wi and length li of each piece.
    wi, li = [int(x) for x in input().split()]
    sum_area += wi * li
# The output should be the integer L = area/W
print(sum_area // w)
