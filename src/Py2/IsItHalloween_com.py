# IsItHalloween.com
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/isithalloween
from sys import stdin, stdout
month, day = stdin.readline().split()
if month == "OCT" and day == "31":
    stdout.write("yup")
elif month == "DEC" and day == "25":
    stdout.write("yup")
else:
    stdout.write("nope")
