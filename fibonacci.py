#!/usr/bin/env python
# coding: utf-8

"""
memo - это декоратор для оптимизиции алгоритма поиска чисел Фибоначчи.
Оптимизация проведена при помощи кэширования предыдущих результатов
"""


def memo(f):
    cash = {}

    def inner(n):
        if n not in cash:
            cash[n] = f(n)
        return cash[n]

    return inner


def fibonacci(n):
    assert n >= 0
    first, second = 0, 1
    for i in range(n - 1):
        first, second = second, first + second
    return second


def main():
    number = int(input())
    print(memo(fibonacci)(number))


if __name__ == "__main__":
    main()
