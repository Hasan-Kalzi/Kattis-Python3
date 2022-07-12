# IsItHalloween.com
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/isithalloween

month, day = input().split(" ")
if month == "OCT" and day == "31":
    print("yup")
elif month == "DEC" and day == "25":
    print("yup")
else:
    print("nope")
