# Weak Vertices
# Solution by Hasan Kalzi 23-10-2020
# Link to problem i Kattis: https://open.kattis.com/problems/weakvertices

while True:
    matrix_size = int(input())
    if matrix_size == -1:
        break
    matrix = []
    # fill the matrix
    for _ in range(matrix_size):
        matrix.append([int(x) for x in input().split()])
    # find all neighbours to the current vertex
    for i in range(matrix_size):
        temp = []
        for j in range(matrix_size):
            if matrix[i][j] == 1:
                temp.append(j)
        if sum(matrix[i]) < 2:
            print(i, end=" ")
            continue
        # check if the neighbours to i vertex are neighbours
        check = 0
        for j in range(len(temp)):
            for k in range(j + 1, len(temp)):
                if matrix[temp[j]][temp[k]] == 1:
                    check += 1
                    continue
        if check == 0:
            print(i, end=" ")

    print()
