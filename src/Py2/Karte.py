# Karte
# Solution by Hasan Kalzi 26-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/karte
from sys import stdin, stdout

card_set = [[1] * 13, [1] * 13, [1] * 13, [1] * 13]
value = stdin.readline().strip()
no_print = 0
for i in range(0, len(value), 3):
    if value[i] == 'P':
        j = 0
    elif value[i] == 'K':
        j = 1
    elif value[i] == 'H':
        j = 2
    else:
        j = 3
    card_set[j][int(value[i + 1:i + 3]) - 1] -= 1
    if card_set[j][int(value[i + 1:i + 3]) - 1] < 0:
        stdout.write("GRESKA")
        no_print = 1
        break
if no_print == 0:
    for set_ in card_set:
        stdout.write(str(sum(set_))+" ")
