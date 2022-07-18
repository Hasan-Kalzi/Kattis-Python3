# No Duplicates
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/nodup

values = input().split()
x = 0
while x <= len(values) - 1:
    if values[x] in values[x + 1:]:
        print("no")
        break
    if x == len(values) - 1:
        print("yes")
    x += 1
