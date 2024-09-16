"""
1. Дано рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за
алфавітом, в стовпчик.
"""


import re


def main(def_text):
    def_str = def_text.split()
    def_out = ""
    for i in sorted(def_str, key=lambda x: x.lower()):
        def_out = def_out + " " + i
    return def_out


text = str(input('Enter text: '))
result = main(text)
print('\n'.join(re.split(r'\s+', result)))
