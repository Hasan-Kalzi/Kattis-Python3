# Relocation
# Solution by Hasan Kalzi 21-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/relocation
import sys

# The first line has two positive space-separated integers N and Q: the number of companies the app tracks (2≤N≤100000)
# , and the number of requests to process (1≤Q≤100000).
# after range is the inserted values of e,f,c: int(sys.stdin.readline())
n, q = [int(_) for _ in sys.stdin.readline().split()]
companies_location = [int(_) for _ in sys.stdin.readline().split()]
for i in range(q):
    # take the order values
    order, target1, target2 = [int(_) for _ in sys.stdin.readline().split()]
    # processing order type 1
    if order == 1:
        companies_location[target1 - 1] = target2
    # processing order type 2
    else:
        sys.stdout.write(str(abs(companies_location[target1 - 1] - companies_location[target2 - 1]))+ "\n")
