# Trik
# Solution by Hasan Kalzi 08-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/trik

x = 1

for elem in input():
    if elem == "A" and x == 1:
        x = 2
    elif elem == "A" and x == 2:
        x = 1
    elif elem == "B" and x == 2:
        x = 3
    elif elem == "B" and x == 3:
        x = 2
    elif elem == "C" and x == 3:
        x = 1
    elif elem == "C" and x == 1:
        x = 3

print(x)
