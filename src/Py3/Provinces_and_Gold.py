# Provinces and Gold
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/provincesandgold

# The input consists of a single test case on a single line, which contains three non-negative integers G, S, C
# (G+S+C≤5) indicating the number of Golds, Silvers, and Coppers Jake draws in his hand.
gold, silver, copper = [float(x) for x in input().split()]
in_hand = int(gold) * 3 + int(silver) * 2 + int(copper)
# the best of victory cards in Dominion:
if in_hand >= 8:
    print("Province ", end="or ")
elif in_hand >= 5:
    print("Duchy ", end="or ")
elif in_hand >= 2:
    print("Estate ", end="or ")
if in_hand >= 6:
    print("Gold")
elif in_hand >= 3:
    print("Silver")
else:
    print("Copper")
