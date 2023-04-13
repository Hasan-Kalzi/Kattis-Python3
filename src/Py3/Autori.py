# Autori
# Solution by Hasan Kalzi 08-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/autori

# Use a list comprehension to extract the first letter of each element after splitting the input string
letters = [elem[0] for elem in input().split("-")]

# Concatenate the list of letters into a single string and print it
print("".join(letters))
