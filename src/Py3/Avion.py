# Avion
# Solution by Hasan Kalzi 22-10-2020
# Link to the problem in Kattis: https://open.kattis.com/problems/avion

# Create a list of indexes where "FBI" is found in the input strings
indexes = [str(i) for i in range(1,6) if input().find("FBI") != -1]

# Check if the list is not empty, meaning that "FBI" was found in at least one input string
if indexes:
    # Print the indexes separated by spaces using join()
    print(" ".join(indexes))
else:
    # Print "HE GOT AWAY!" if "FBI" was not found in any input string
    print("HE GOT AWAY!")
