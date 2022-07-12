# I've Been Everywhere, Man
# Solution by Hasan Kalzi 27-09-2020
# Link to problem in Kattis: https://open.kattis.com/problems/everywhere

for _ in range(int(input())):
    cities = []
    for _ in range(int(input())):
        city = input()
        if city not in cities:
            cities.append(city)
    print(len(cities))
