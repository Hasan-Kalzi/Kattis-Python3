# Harshad Numbers
# Solution by Hasan Kalzi 21-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/harshadnumbers


def harshad_numbers(number):
    sum_numbers = 0
    for i in number:
        sum_numbers += int(i)
    # if the rest of division is zero that is the number we want
    if int(number) % sum_numbers == 0:
        print(number)
    # if the rest is not zero add 1 to the number and check the new number
    else:
        harshad_numbers(str(int(number) + 1))


inserted_number = input()
harshad_numbers(inserted_number)
