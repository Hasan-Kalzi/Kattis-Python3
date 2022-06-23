# Cetvrta
# Solution by Hasan Kalzi 08-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/cetvrta

values = ""
for i in range(3):
    values = values + input() + " "
values = values.split(" ")
if values[0] == values[2]:
    x = values[4]
elif values[0] == values[4]:
    x = values[2]
else:
    x = values[0]
if values[1] == values[3]:
    y = values[5]
elif values[1] == values[5]:
    y = values[3]
else:
    y = values[1]
print(x, y)
