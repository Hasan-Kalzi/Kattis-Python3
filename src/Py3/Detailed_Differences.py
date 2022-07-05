# Detailed Differences
# Solution by Hasan Kalzi 22-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/detaileddifferences

# after range is the value of inserted number of cases: int(input())
for _ in range(int(input())):
    word1 = input()
    word2 = input()
    similarities_and_differences = ""
    # compare every character in both word in sequence and add the result to similarities and differences as described.
    for j in range(len(word1)):
        if word1[j] == word2[j]:
            similarities_and_differences += "."
        else:
            similarities_and_differences += "*"
    print(word1 + "\n" + word2 + "\n" + similarities_and_differences + "\n")
