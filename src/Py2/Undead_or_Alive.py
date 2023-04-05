# Undead or Alive
# Solution by Hasan Kalzi 05-04-2023
# Link to problem in Kattis: https://open.kattis.com/problems/undeadoralive
from sys import stdin,stdout

sentence = stdin.readline()
s,f = 0,0
if ":(" in sentence:
    f = 1
if ":)" in sentence:
    s = 1
if s == 1 and f == 1:
    stdout.write("double agent")
elif s == 1:
    stdout.write("alive")
elif f == 1:
    stdout.write("undead")
else:
    stdout.write("machine")
