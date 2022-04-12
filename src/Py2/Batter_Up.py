# Batter Up
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/batterup
from __future__ import division
from sys import stdin, stdout

stdin.readline()
game_values = [int(_) for _ in stdin.readline().strip().split() if _ != '-1']
stdout.write(str(sum(game_values) / len(game_values)))
