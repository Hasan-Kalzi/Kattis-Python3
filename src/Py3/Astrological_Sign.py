# Astrological Sign
# Solution by Hasan Kalzi 10-03-2021
# Link to problem i Kattis: https://open.kattis.com/problems/astrologicalsign

# Importing the necessary libraries
from sys import stdin,stdout

# Reading the input and iterating through the test cases
for _ in range(int(stdin.readline())):
    # Reading the day and month from input
    day,month = stdin.readline().split()
    # Converting day from string to integer
    day = int(day)

    # Checking for Aries sign
    if month == "Mar" and day >= 21 or month == "Apr" and day <= 20:
        stdout.write("Aries\n")
    # Checking for Taurus sign
    elif month == "Apr" and day >= 21 or month == "May" and day <= 20:
        stdout.write("Taurus\n")
    # Checking for Gemini sign
    elif month == "May" and day >= 21 or month == "Jun" and day <= 21:
        stdout.write("Gemini\n")
    # Checking for Cancer sign
    elif month == "Jun" and day >= 22 or month == "Jul" and day <= 22:
        stdout.write("Cancer\n")
    # Checking for Leo sign
    elif month == "Jul" and day >= 23 or month == "Aug" and day <= 22:
        stdout.write("Leo\n")
    # Checking for Virgo sign
    elif month == "Aug" and day >= 23 or month == "Sep" and day <= 21:
        stdout.write("Virgo\n")
    # Checking for Libra sign
    elif month == "Sep" and day >= 22 or month == "Oct" and day <= 22:
        stdout.write("Libra\n")
    # Checking for Scorpio sign
    elif month == "Oct" and day >= 23 or month == "Nov" and day <= 22:
        stdout.write("Scorpio\n")
    # Checking for Sagittarius sign
    elif month == "Nov" and day >= 23 or month == "Dec" and day <= 21:
        stdout.write("Sagittarius\n")
    # Checking for Capricorn sign
    elif month == "Dec" and day >= 22 or month == "Jan" and day <= 20:
        stdout.write("Capricorn\n")
    # Checking for Aquarius sign
    elif month == "Jan" and day >= 21 or month == "Feb" and day <= 19:
        stdout.write("Aquarius\n")
    # Checking for Pisces sign
    elif month == "Feb" and day >= 20 or month == "Mar" and day <= 20:
        stdout.write("Pisces\n")
