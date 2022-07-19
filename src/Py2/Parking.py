# Parking
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/parking2
from sys import stdin, stdout
# Whatever the point he chose to park his car he will walk the same distance back to his car
# if he goes into stores in order

# after range is the inserted number of cases: int(input())
for _ in range(int(stdin.readline())):
    number_of_stores = int(stdin.readline())
    stores_positions = sorted([int(_) for _ in stdin.readline().split()])
    # the min distance equals with difference between the position of the last store and the position of the first one
    # the answer * 2 because he will go back to his car after reaching the end
    min_distance = (stores_positions[number_of_stores - 1] - stores_positions[0])*2
    stdout.write(str(min_distance)+'\n')
