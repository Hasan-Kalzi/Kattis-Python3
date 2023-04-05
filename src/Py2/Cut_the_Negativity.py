# Cut the Negativity
# Solution by Hasan Kalzi 05-04-2023
# Link to problem in Kattis: https://open.kattis.com/problems/cutthenegativity
from sys import stdout,stdin


class FlightCost:
    def __init__(self,start,end,cost):
        self.start = start
        self.end = end
        self.cost = cost


if __name__ == '__main__':
    price_list = []
    n = int(stdin.readline())

    for j in range(n):
        line = [int(_) for _ in stdin.readline().split()]
        for i in range(n):
            if line[i] > 0:
                price_list.append(FlightCost(j + 1,i + 1,line[i]))
    stdout.write(str(len(price_list)) + '\n')
    for price in price_list:
        stdout.write(str(price.start) + ' ' + str(price.end) + ' ' + str(price.cost) + '\n')
