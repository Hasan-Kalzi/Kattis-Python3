# Batter Up
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/batterup

counter = 0
points = 0
input()
game_values = [int(x) for x in input().split()]
for elem in game_values:
    if elem != -1:
        points += elem
        counter += 1
print(points / counter)
