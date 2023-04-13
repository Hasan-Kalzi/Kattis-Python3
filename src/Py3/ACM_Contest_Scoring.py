# ACM Contest Scoring
# Solution by Hasan Kalzi 05-04-2021
# Link to problem in https://open.kattis.com/problems/acm

# Import the standard input/output module
from sys import stdin, stdout

# Create an empty dictionary to store the answers
answers = {}

# Loop until the user enters -1 as input
while 1:
    # Read a line of input from standard input
    line = stdin.readline()

    # If the input is -1, break out of the loop
    if line == "-1\n":
        break
    else:
        # Split the input line into three parts: minutes, problem, and status
        m, problem, status = line.split()

        # If the problem has not been encountered before, add it to the dictionary
        if problem not in answers:
            # Initialize the problem's score and number of correct answers
            answers[problem] = [0, 0]

        # If the answer is wrong, add 20 penalty points to the problem's score
        if status == "wrong":
            answers[problem][0] += 20
        # If the answer is correct, add the number of minutes to the problem's score
        else:
            answers[problem][0] += int(m)
            # Mark the problem as having a correct answer
            answers[problem][1] = 1

# Initialize variables for the final score and number of correct answers
score, right = 0, 0

# Loop through the dictionary of answers
for answer in answers:
    # If the problem has a correct answer, add its score to the total score and increment the number of correct answers
    if answers[answer][1] == 1:
        right += 1
        score += answers[answer][0]

# Write the number of correct answers and total score to standard output
stdout.write(str(right) + ' ' + str(score))
