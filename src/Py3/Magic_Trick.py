# Magic Trick
# Solution by Hasan Kalzi 21-06-2021
# # Link to problem in Kattis6: https://open.kattis.com/problems/magictrick
from sys import stdin, stdout

original, = stdin.readline(),
original_l, trimmed_l = len(original), len("".join(set(original)))
if original_l == trimmed_l:
    stdout.write("1")
else:
    stdout.write("0")
