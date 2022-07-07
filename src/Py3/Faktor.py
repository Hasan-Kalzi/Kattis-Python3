# Faktor
# Solution by Hasan Kalzi 27-09-2020
# Link to problem i Kattis: https://open.kattis.com/problems/faktor
import math

faktor = input().split(" ")
print(math.ceil(int(faktor[0]) * (int(faktor[1]) - 1 + 0.00000000001)))
