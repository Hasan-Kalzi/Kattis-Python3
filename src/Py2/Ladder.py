# Ladder
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/ladder
from __future__ import division
from sys import stdin, stdout
from math import sin, radians
#  The desired ladder have length h/sin(v)  h: is the wall height and v: the angle from the ground
wall_height, angle = map(int, stdin.readline().split())

if wall_height/sin(radians(angle)) > int(wall_height/sin(radians(angle))):
    stdout.write(str(int(wall_height/sin(radians(angle))+1)))
else:
    stdout.write(str(int(wall_height/sin(radians(angle)))))
