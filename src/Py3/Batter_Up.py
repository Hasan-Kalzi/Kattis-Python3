# Batter Up
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/batterup

# Skip first input (number of at-bats)
_ = input()

# Create a list of at-bat values
game_values = list(map(int, input().split()))

# Count the number of non-strikeout at-bats and calculate the total points scored
counter = len([x for x in game_values if x != -1])
points = sum([x for x in game_values if x != -1])

# Print the average number of points per non-strikeout at-bat
print(points / counter)
