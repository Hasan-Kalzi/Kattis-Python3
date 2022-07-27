# Stand on Zanzibar
# Solution by Hasan Kalzi 25-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/zanzibar

# after range is the inserted number of cases: int(input())
for _ in range(int(input())):
    # the lower bound for the number of turtles not born on Zanzibar.
    lower_bound = 0
    values = [int(x) for x in input().split()]
    for i in range(len(values)):
        if values[i] == 0:
            break
        if values[i + 1] > values[i] * 2:
            lower_bound += values[i + 1] - (2 * values[i])
    print(lower_bound)
