"""
2. Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt').
Виділіть з цього рядка ім'я файлу без розширення
"""


import ntpath


def main(text_: str):
    # Отримання файла, без використання ос
    return ntpath.basename(text_)[:ntpath.basename(text).find('.')]


text = str(input('Enter the string: '))
result = main(text)
print(result)

