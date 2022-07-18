# Nasty Hacks
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/nastyhacks


# after range is the inserted number of lines: int(input())
for _ in range(int(input())):
    values = [int(x) for x in input().split()]
    if values[1] - values[0] > values[2]:
        print("advertise")
    elif values[1] - values[0] == values[2]:
        print("does not matter")
    else:
        print("do not advertise")
