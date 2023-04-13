# Importing the necessary modules
from sys import stdin,stdout

# Loop over the number of test cases
for _ in range(int(stdin.readline())):

    # Reading the input values
    k,pq = stdin.readline().split()

    # Converting the input into integers
    p,q = map(int,pq.split('/'))

    # Initializing the answer string
    ans = ''

    # While loop to compute the binary representation of the given rational number
    while p + q > 2:
        if p > q:
            p -= q
            ans += '1'
        else:
            q -= p
            ans += '0'

    # Appending the final bit to the answer string
    ans += '1'

    # Writing the output to stdout
    stdout.write(k + ' ' + str(int(ans[::-1],2)) + '\n')

