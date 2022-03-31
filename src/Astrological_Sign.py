# Astrological Sign
# Solution by Hasan Kalzi 10-03-2021
# Link to problem i Kattis: https://open.kattis.com/problems/astrologicalsign
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    day, month = stdin.readline().split()
    day = int(day)
    if month == "Mar" and day >= 21:
        stdout.write("Aries\n")
    elif month == "Apr" and day <= 20:
        stdout.write("Aries\n")

    elif month == "Apr" and day >= 21:
        stdout.write("Taurus\n")
    elif month == "May" and day <= 20:
        stdout.write("Taurus\n")

    elif month == "May" and day >= 21:
        stdout.write("Gemini\n")
    elif month == "Jun" and day <= 21:
        stdout.write("Gemini\n")

    elif month == "Jun" and day >= 22:
        stdout.write("Cancer\n")
    elif month == "Jul" and day <= 22:
        stdout.write("Cancer\n")

    elif month == "Jul" and day >= 23:
        stdout.write("Leo\n")
    elif month == "Aug" and day <= 22:
        stdout.write("Leo\n")

    elif month == "Aug" and day >= 23:
        stdout.write("Virgo\n")
    elif month == "Sep" and day <= 21:
        stdout.write("Virgo\n")

    elif month == "Sep" and day >= 22:
        stdout.write("Libra\n")
    elif month == "Oct" and day <= 22:
        stdout.write("Libra\n")

    elif month == "Oct" and day >= 23:
        stdout.write("Scorpio\n")
    elif month == "Nov" and day <= 22:
        stdout.write("Scorpio\n")

    elif month == "Nov" and day >= 23:
        stdout.write("Sagittarius\n")
    elif month == "Dec" and day <= 21:
        stdout.write("Sagittarius\n")

    elif month == "Dec" and day >= 22:
        stdout.write("Capricorn\n")
    elif month == "Jan" and day <= 20:
        stdout.write("Capricorn\n")

    elif month == "Jan" and day >= 21:
        stdout.write("Aquarius\n")
    elif month == "Feb" and day <= 19:
        stdout.write("Aquarius\n")

    elif month == "Feb" and day >= 20:
        stdout.write("Pisces\n")
    elif month == "Mar" and day <= 20:
        stdout.write("Pisces\n")
