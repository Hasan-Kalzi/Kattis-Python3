# Tai's formula
# Solution by Hasan Kalzi 23-10-2020
# Link to problem in Kattis: https://open.kattis.com/problems/taisformula

# A matrix to save the inserted values
matrix = []
# A list to save all part of area
area = []
# after range is the inserted number of glucose samples: int(input())
for _ in range(int(input())):
    matrix.append([float(x) for x in input().split()])
for i in range(len(matrix) - 1):
    area.append((((matrix[i][1] + matrix[i + 1][1]) / 2) * (matrix[i + 1][0] - matrix[i][0])) / 1000)
print(sum(area))
