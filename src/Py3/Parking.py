# Parking
# Solution by Hasan Kalzi 17-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/parking2

# Whatever the point he chose to park his car he will walk the same distance back to his car
# if he goes into stores in order

# after range is the inserted number of cases: int(input())
for _ in range(int(input())):
    number_of_stores = int(input())
    stores_positions = sorted([int(x) for x in input().split()])
    # the min distance equals with difference between the position of the last store and the position of the first one
    # the answer * 2 because he will go back to his car after reaching the end
    min_distance = (stores_positions[number_of_stores - 1] - stores_positions[0])*2
    print(min_distance)
