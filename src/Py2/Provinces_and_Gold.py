# coding=utf-8
# Provinces and Gold
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/provincesandgold
from sys import stdin, stdout
# The input consists of a single test case on a single line, which contains three non-negative integers G, S, C
# (G+S+C≤5) indicating the number of Golds, Silvers, and Coppers Jake draws in his hand.
gold, silver, copper = map(int, stdin.readline().split())
in_hand = gold * 3 + silver * 2 + copper
# the best of victory cards in Dominion:
if in_hand >= 8:
    stdout.write("Province or ")
elif in_hand >= 5:
    stdout.write("Duchy or ")
elif in_hand >= 2:
    stdout.write("Estate or ")
if in_hand >= 6:
    stdout.write("Gold")
elif in_hand >= 3:
    stdout.write("Silver")
else:
    stdout.write("Copper")
