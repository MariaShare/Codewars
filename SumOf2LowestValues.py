# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:07:18 2022

@author: Shadrina Maria
"""

'''Решение задачи _Sum of two lowest positive integers_
Solution of task _Sum of two lowest positive integers_
'''
"Возвращает сумму двух наименьших чисел в массиве"
def sum_two_smallest_numbers(numbers):
    "Присвоение начальных значений массива с исключением повторов"
    min1 = numbers[0]
    "Обход массива от начала"
    for i in range(len(numbers)):
        if numbers[i] < min1:
            min1 = numbers[i]
    "Обход массива с конца"
    min2 = numbers[-1]
    for i in range(len(numbers)):
        if numbers[i] < min2 and numbers[i] != min1:
            min2 = numbers[i]
    return min1 + min2

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))