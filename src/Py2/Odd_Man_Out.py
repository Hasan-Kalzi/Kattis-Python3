# Odd Man Out
# Solution by Hasan Kalzi 21-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/oddmanout
from sys import stdin, stdout

# The first line of input gives the number of cases,  N
# after range is the inserted values of N: int(sys.stdin.readline())
for i in range(int(stdin.readline())):
    # One line containing the value G the number of guests.
    g = int(stdin.readline())
    # One line containing a space-separated list of G integers. Each integer C indicates the invitation code of a guest.
    guests_numbers = stdin.readline().split()
    for j in range(g):
        if g == 0:
            if guests_numbers[j] not in guests_numbers[j + 1:len(guests_numbers)]:
                stdout.write("Case #" + str(i + 1) + ": " + guests_numbers[j] + "\n")
                break
        else:
            if guests_numbers[j] not in guests_numbers[j + 1:len(guests_numbers)] \
                    and guests_numbers[j] not in guests_numbers[0:j]:
                stdout.write("Case #" + str(i + 1) + ": " + guests_numbers[j] + "\n")
                break
