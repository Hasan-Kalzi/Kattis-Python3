# Greetings!
# Solution by Hasan Kalzi 14-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/greetings2
import sys

s = sys.stdin.readline()
sys.stdout.write("h" + "e" * (len(s[1:len(s) - 2])*2) + "y")
