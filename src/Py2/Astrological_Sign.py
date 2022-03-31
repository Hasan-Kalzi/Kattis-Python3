# Astrological Sign
# Solution by Hasan Kalzi 23-12-2020
# Link to problem i Kattis: https://open.kattis.com/problems/astrologicalsign
import sys

for _ in range(int(sys.stdin.readline())):
    day, month = sys.stdin.readline().split()
    day = int(day)
    if month == "Mar" and day >= 21:
        sys.stdout.write("Aries\n")
    elif month == "Apr" and day <= 20:
        sys.stdout.write("Aries\n")

    elif month == "Apr" and day >= 21:
        sys.stdout.write("Taurus\n")
    elif month == "May" and day <= 20:
        sys.stdout.write("Taurus\n")

    elif month == "May" and day >= 21:
        sys.stdout.write("Gemini\n")
    elif month == "Jun" and day <= 21:
        sys.stdout.write("Gemini\n")

    elif month == "Jun" and day >= 22:
        sys.stdout.write("Cancer\n")
    elif month == "Jul" and day <= 22:
        sys.stdout.write("Cancer\n")

    elif month == "Jul" and day >= 23:
        sys.stdout.write("Leo\n")
    elif month == "Aug" and day <= 22:
        sys.stdout.write("Leo\n")

    elif month == "Aug" and day >= 23:
        sys.stdout.write("Virgo\n")
    elif month == "Sep" and day <= 21:
        sys.stdout.write("Virgo\n")

    elif month == "Sep" and day >= 22:
        sys.stdout.write("Libra\n")
    elif month == "Oct" and day <= 22:
        sys.stdout.write("Libra\n")

    elif month == "Oct" and day >= 23:
        sys.stdout.write("Scorpio\n")
    elif month == "Nov" and day <= 22:
        sys.stdout.write("Scorpio\n")

    elif month == "Nov" and day >= 23:
        sys.stdout.write("Sagittarius\n")
    elif month == "Dec" and day <= 21:
        sys.stdout.write("Sagittarius\n")

    elif month == "Dec" and day >= 22:
        sys.stdout.write("Capricorn\n")
    elif month == "Jan" and day <= 20:
        sys.stdout.write("Capricorn\n")

    elif month == "Jan" and day >= 21:
        sys.stdout.write("Aquarius\n")
    elif month == "Feb" and day <= 19:
        sys.stdout.write("Aquarius\n")

    elif month == "Feb" and day >= 20:
        sys.stdout.write("Pisces\n")
    elif month == "Mar" and day <= 20:
        sys.stdout.write("Pisces\n")
