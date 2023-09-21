# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""
numbers = int(input("Введите число: "))


def sum_numbers(numbers: int):
    s = 0
    len_numbers = len(str(numbers))
    assert len_numbers == 4, "Число не четырехзначное"

    while len_numbers > 0:
        s += numbers % 10
        numbers = numbers // 10
        len_numbers -= 1

    return s


print(sum_numbers(numbers))