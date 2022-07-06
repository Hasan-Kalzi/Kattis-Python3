# Electrical outlets
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/electricaloutlets
import sys

# after range is the inserted number of cups: int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline())):
    values = [int(_) for _ in sys.stdin.readline().split()]
    # The first value of the list is not included and we add 2 because the first one can provide
    # without connection. and for the same reason the first value is not calculated.
    sys.stdout.write(str(sum(values[1:len(values)]) - len(values) + 2) + "\n")
