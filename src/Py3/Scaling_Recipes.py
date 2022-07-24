# Scaling Recipes
# Solution by Hasan Kalzi 29-03-2021
# Link to problem in https://open.kattis.com/problems/recipes
import sys

for i in range(1, int(sys.stdin.readline()) + 1):
    ingredients = []
    scale = 0.0
    sys.stdout.write("Recipe # " + str(i) + '\n')
    r, p, d = map(int, sys.stdin.readline().split())
    factor = d / p
    for j in range(r):
        ingredients.append(sys.stdin.readline().split())
        if float(ingredients[j][2]) == 100:
            scale = float(ingredients[j][1]) * factor
    for ing in ingredients:
        sys.stdout.write(ing[0] + ' ' + str("{:.1f}".format((float(ing[2]) * scale) / 100)) + '\n')
    sys.stdout.write("----------------------------------------\n")
