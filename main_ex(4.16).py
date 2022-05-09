"""
16. Дано цілочисельний список, що не містить однакових чисел. Перевірити, чи утворюють його
елементи арифметичну прогресію (A, A + D, A + 2 • D, A + 3 • D, ....). Якщо утворюють, то вивести
різницю прогресії, якщо ні - вивести 0.
"""
from operator import sub


def main(r_):
    r = set(map(sub, arr[1:], arr))
    return r.pop() if len(r) == 1 else 0


arr = list(map(int, input("Введите cписок: ").split()))
result = main(arr)
print(result)
input()