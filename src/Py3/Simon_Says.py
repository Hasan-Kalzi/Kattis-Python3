# Simon Says
# Solution by Hasan Kalzi 17-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/simonsays

number_of_lines = int(input())
for _ in range(number_of_lines):
    text = input()
    if "Simon says" in text:
        print(text[11:])
