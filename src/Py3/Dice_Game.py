# Dice Game
# Solution by Hasan Kalzi 24-03-2021
# Link to problem in https://open.kattis.com/problems/dicegame
import sys

gunnar = sum(map(int, sys.stdin.readline().split()))
emma = sum(map(int, sys.stdin.readline().split()))
if gunnar > emma:
    sys.stdout.write("Gunnar")
elif gunnar == emma:
    sys.stdout.write("Tie")
else:
    sys.stdout.write("Emma")
