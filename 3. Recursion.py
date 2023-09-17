"""Базовый и рекурсивный случаи"""


def countdown(i):
    print(i)
    if i <= 0:
        return i
    else:
        countdown(i-1)


countdown(5)