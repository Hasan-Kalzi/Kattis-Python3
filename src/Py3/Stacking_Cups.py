# Stacking Cups
# Solution by Hasan Kalzi 25-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/cups

list_ = []
# after range is the inserted number of cups: int(input())
for _ in range(int(input())):
    cup_i = input().split()
    if cup_i[0].isdigit():
        list_.append([int(cup_i[0]) / 2, cup_i[1]])
    else:
        list_.append([int(cup_i[1]), cup_i[0]])
list_.sort()
for element in list_:
    print(element[1])
