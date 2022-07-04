# Cudoviste
# Solution by Hasan Kalzi 23-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/cudoviste


rows, columns = map(int, input().split())
input_list = []
for i in range(rows):
    input_list.append(input())
all_cases = [0] * 5
for i in range(columns - 1):
    for j in range(rows - 1):
        a = input_list[j][i]
        b = input_list[j + 1][i]
        c = input_list[j][i + 1]
        d = input_list[j + 1][i + 1]
        if a == '#' or b == '#' or c == '#' or d == '#':
            continue
        car_squashed = 0
        if a == "X":
            car_squashed += 1
        if b == "X":
            car_squashed += 1
        if c == "X":
            car_squashed += 1
        if d == "X":
            car_squashed += 1
        all_cases[car_squashed] += 1
for case in all_cases:
    print(case)
