# Echo Echo Echo
# Solution by Hasan Kalzi 21-06-2021
# # Link to problem in Kattis6: https://open.kattis.com/problems/echoechoecho
from sys import stdin, stdout

stdout.write(((stdin.readline().strip() + " ") * 3).strip())