# Right-of-Way
# Solution by Hasan Kalzi 15-04-2021
# Link to problem in Kattis: https://open.kattis.com/problems/vajningsplikt/en
from sys import stdin, stdout

# right, left , opposite
sets = [["East", "West", "North"], ["North", "South", "West"], ["South", "North", "East"], ["West", "East", "South"]]

directions = stdin.readline().strip().split()
if directions[0] == "South":
    i = 0
elif directions[0] == "East":
    i = 1
elif directions[0] == "West":
    i = 2
else:
    i = 3
if directions[1] == sets[i][1]:
    if directions[2] == sets[i][0] or directions[2] == sets[i][2]:
        stdout.write("Yes\n")
    else:
        stdout.write("No\n")
elif directions[1] == sets[i][2]:
    if directions[2] == sets[i][0]:
        stdout.write("Yes\n")
    else:
        stdout.write("No\n")
else:
    stdout.write("No\n")
