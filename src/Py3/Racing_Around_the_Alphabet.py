# Racing Around the Alphabet
# Solution by Hasan Kalzi 21-11-2020
# Link to problem in Kattis: https://open.kattis.com/problems/racingalphabet
import sys

alphabet_circle = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z", " ", "'"]
# circumference /28 = pi*60 / 28
alphabet_length = 6.7319842576924140824199501070275
# The input begins with a number N, (1≤N≤20) giving the number of aphorisms to follow
# after range is the inserted values of N: int(sys.stdin.readline())
for _ in range(int(sys.stdin.readline())):
    given_string = sys.stdin.readline()
    # Standing at the position of first letter in the circle.
    current_position = alphabet_circle.index(given_string[0])
    elapsed_time = 0
    for alphabet in given_string[0:len(given_string) - 1]:
        # Choose the shortest way to the next letter.
        choice = abs(current_position - alphabet_circle.index(alphabet))
        if choice > 14:
            choice = 28 - choice
        # calculate the elapsed time and add it
        elapsed_time += (alphabet_length * choice / 15) + 1
        current_position = alphabet_circle.index(alphabet)
    sys.stdout.write("%.10f" % elapsed_time + "\n")
