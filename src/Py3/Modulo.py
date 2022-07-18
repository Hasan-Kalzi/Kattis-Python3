# Modulo
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/modulo

distinct_list = []
for _ in range(10):
    number = int(input())
    if number >= 42:
        number = number % 42
    if number not in distinct_list:
        distinct_list.append(number)
print(len(distinct_list))
