# Judging Moose
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/judgingmoose

left, right = [int(x) for x in input().split()]
if left == 0 and right == 0:
    print("Not a moose")
elif left == right:
    print("Even", left * 2)
else:
    print("Odd", max(left, right) * 2)
