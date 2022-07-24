# Roaming Romans
# Solution by Hasan Kalzi 16-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/romans


english_miles = float(input())
# calculating the inserted english miles in roman paces.
roman_paces = (english_miles * 1000 * 5280) / 4854
# printing the rounded result.
print(round(roman_paces))
