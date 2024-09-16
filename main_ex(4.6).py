"""
6. Дано рядок. Якщо в цьому рядку буква f зустрічається тільки один раз, виведіть її індекс. Якщо
вона зустрічається два і більше разів, виведіть індекси її першої і останньої появи. Якщо буква f в
цьому рядку не зустрічається, нічого не виводьте.
"""


def main(text: str):
    first_index = text.find('f')
    last_index = text.rfind('f')
    if first_index != -1 and last_index != -1 and first_index != last_index:
        return first_index, last_index
    if first_index != -1 and last_index != -1 and first_index == last_index:
        return first_index
    if first_index != -1 and last_index == -1:
        return first_index
    if first_index == -1 and last_index != -1:
        return last_index
    if first_index == -1 and last_index == -1:
        return ' '


text_ = str(input('Введіть рядок: '))
result = main(text_)
print(result)
input()
