"""
11. Дано список. Вивести спочатку всі негативні елементи, а потім всі інші.
"""


def main(def_list):
    return list(filter(lambda x: x < 0, def_list)) + \
           list(filter(lambda x: x >= 0, def_list))


print('Enter the list: ')
lst_ = []
for i in range(int(input())):
    lst_.append(int(input()))
result = main(lst_)
print(result)