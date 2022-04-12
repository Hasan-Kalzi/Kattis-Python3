# Avion
# Solution by Hasan Kalzi 22-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/avion

nothing = True
for i in range(1, 6):
    if "FBI" in input():
        print(i, end=" ")
        nothing = False
if nothing:
    print("HE GOT AWAY!")
