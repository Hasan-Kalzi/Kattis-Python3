# coding=utf-8
# Östgötska
# Solution by Hasan Kalzi 07-04-2021
# Link to problem in https://open.kattis.com/problems/ostgotska
from __future__ import division
from sys import stdin, stdout

ae = 0
input_words = stdin.readline().strip().split()
for word in input_words:
    if "ae" in word:
        ae += 1
if ae/len(input_words) >= 0.4:
    stdout.write("dae ae ju traeligt va")
else:
    stdout.write("haer talar vi rikssvenska")
