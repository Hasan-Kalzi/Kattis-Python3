# Hissing Microphone
# Solution by Hasan Kalzi 03-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/hissingmicrophone
from sys import stdin, stdout
if "ss" in stdin.readline():
    stdout.write("hiss")
else:
    stdout.write("no hiss")
