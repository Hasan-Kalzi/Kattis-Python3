# Poker Hand
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/pokerhand
from sys import stdin, stdout


def check_max(cards, j):
    hand_power = 1
    for k in range(j + 1, 5):
        if cards[j][0] == cards[k][0]:
            hand_power += 1
    return hand_power


cards_in_hand = stdin.readline().strip().split()
max_hand_power = 1
# compare every card with the other card
# the first card with other four cards
# the second card with other tree cards
# ...
for i in range(5):
    max_hand_power = max(max_hand_power, check_max(cards_in_hand, i))
    # if there is no hope getting max than the current value break to save time
    if max_hand_power > 5 - i:
        break
# printing the result
stdout.write(str(max_hand_power))
