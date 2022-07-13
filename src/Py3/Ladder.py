# Ladder
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/ladder


import math
#  The desired ladder have length h/sin(v)  h: is the wall height and v: the angle from the ground
wall_height, angle = [int(x) for x in input().split()]

if wall_height/math.sin(math.radians(angle)) > int(wall_height/math.sin(math.radians(angle))):
    print(int(wall_height/math.sin(math.radians(angle))+1))
else:
    print(int(wall_height/math.sin(math.radians(angle))))
