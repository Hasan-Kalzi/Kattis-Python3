# Bela
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/bela

game_values = input().split(" ")
score = 0
for _ in range(int(game_values[0])*4):
    values = input()
    if values[0] == "A":
        score += 11
    elif values[0] == "K":
        score += 4
    elif values[0] == "Q":
        score += 3
    elif values[0] == "J":
        if values[1] == game_values[1]:
            score += 20
        else:
            score += 2
    elif values[0] == "T":
        score += 10
    elif values[0] == "9":
        if values[1] == game_values[1]:
            score += 14
print(score)
