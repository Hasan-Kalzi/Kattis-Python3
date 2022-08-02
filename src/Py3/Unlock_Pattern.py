# Unlock Pattern
# Solution by Hasan Kalzi 25-06-2021
# Link to problem in Kattis: https://open.kattis.com/problems/differentdistances
from sys import stdin, stdout

pattern = []
distance = 0
for _ in range(3):
    a, b, c = map(int, stdin.readline().split())
    pattern.append(a)
    pattern.append(b)
    pattern.append(c)
for i in range(1, 9):
    if pattern.index(i) == 0 and pattern.index(i + 1) == 8:
        distance += 2 * 1.4142135623730950488016887242097
    elif pattern.index(i) == 8 and pattern.index(i + 1) == 0:
        distance += 2 * 1.4142135623730950488016887242097
    elif pattern.index(i) == 2 and pattern.index(i + 1) == 6:
        distance += 2 * 1.4142135623730950488016887242097
    elif pattern.index(i) == 6 and pattern.index(i + 1) == 2:
        distance += 2 * 1.4142135623730950488016887242097
    elif pattern.index(i) == 0 and pattern.index(i + 1) == 2:
        distance += 2
    elif pattern.index(i) == 2 and pattern.index(i + 1) == 0:
        distance += 2
    elif pattern.index(i) == 3 and pattern.index(i + 1) == 5:
        distance += 2
    elif pattern.index(i) == 5 and pattern.index(i + 1) == 3:
        distance += 2
    elif pattern.index(i) == 6 and pattern.index(i + 1) == 8:
        distance += 2
    elif pattern.index(i) == 8 and pattern.index(i + 1) == 6:
        distance += 2
    elif pattern.index(i) == 0 and pattern.index(i + 1) == 6:
        distance += 2
    elif pattern.index(i) == 6 and pattern.index(i + 1) == 0:
        distance += 2
    elif pattern.index(i) == 1 and pattern.index(i + 1) == 7:
        distance += 2
    elif pattern.index(i) == 7 and pattern.index(i + 1) == 1:
        distance += 2
    elif pattern.index(i) == 2 and pattern.index(i + 1) == 8:
        distance += 2
    elif pattern.index(i) == 8 and pattern.index(i + 1) == 2:
        distance += 2
    elif pattern.index(i) == 0 and pattern.index(i + 1) == 4:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 4 and pattern.index(i + 1) == 0:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 1 and pattern.index(i + 1) == 3:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 3 and pattern.index(i + 1) == 1:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 1 and pattern.index(i + 1) == 5:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 5 and pattern.index(i + 1) == 1:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 2 and pattern.index(i + 1) == 4:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 4 and pattern.index(i + 1) == 2:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 3 and pattern.index(i + 1) == 7:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 7 and pattern.index(i + 1) == 3:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 4 and pattern.index(i + 1) == 6:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 6 and pattern.index(i + 1) == 4:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 4 and pattern.index(i + 1) == 8:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 8 and pattern.index(i + 1) == 4:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 5 and pattern.index(i + 1) == 7:
        distance += 1.4142135623730950488016887242097
    elif pattern.index(i) == 7 and pattern.index(i + 1) == 5:
        distance += 1.4142135623730950488016887242097

    elif pattern.index(i) == 0 and pattern.index(i + 1) == 5:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 5 and pattern.index(i + 1) == 0:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 2 and pattern.index(i + 1) == 3:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 3 and pattern.index(i + 1) == 2:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 3 and pattern.index(i + 1) == 8:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 8 and pattern.index(i + 1) == 3:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 6 and pattern.index(i + 1) == 5:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 5 and pattern.index(i + 1) == 6:
        distance += 2.2360679774997896964091736687313

    elif pattern.index(i) == 0 and pattern.index(i + 1) == 7:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 7 and pattern.index(i + 1) == 0:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 1 and pattern.index(i + 1) == 6:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 6 and pattern.index(i + 1) == 1:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 1 and pattern.index(i + 1) == 8:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 8 and pattern.index(i + 1) == 1:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 2 and pattern.index(i + 1) == 7:
        distance += 2.2360679774997896964091736687313
    elif pattern.index(i) == 7 and pattern.index(i + 1) == 2:
        distance += 2.2360679774997896964091736687313

    else:
        distance += 1

stdout.write(str(distance))
