# Shopping List (Easy)
# Solution by Hasan Kalzi 12-03-2021
# Link to problem in Kattis: https://open.kattis.com/problems/shoppinglisteasy
import sys


class ShoppingList:
    def __init__(self, item_name, repeated):
        self.item_name = item_name
        self.repeated = repeated


n, m = map(int, sys.stdin.readline().split())
shopping_list = []
first_list_items_names = sys.stdin.readline().split()
first_list_items_names = list(dict.fromkeys(first_list_items_names))
number_item_in_list = 0
for i in range(len(first_list_items_names)):
    shopping_list.append(ShoppingList(first_list_items_names[i], 1))
for i in range(n - 1):
    items_names_other = sys.stdin.readline().split()
    for j in range(len(shopping_list)):
        if first_list_items_names[j] in items_names_other:
            shopping_list[j].repeated += 1
            if shopping_list[j].repeated == n:
                number_item_in_list += 1
sys.stdout.write(str(number_item_in_list) + '\n')
shopping_list = sorted(shopping_list, key=lambda x: x.item_name)
for item in shopping_list:
    if item.repeated >= n:
        sys.stdout.write(item.item_name + '\n')

