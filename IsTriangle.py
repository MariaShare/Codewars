# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 13:48:06 2022

@author: Shadrina Maria
"""

'''Решение задачи _Is this a triangle?_
Solution of task _Is this a triangle?_
'''

"Проверяет может ли существовать треугольник с такими сторонами"
def is_triangle(a, b, c):
    "Используем понятия неравенств треугольника a < b + c, a > |b - c|"
    if a < b + c and a > abs(b - c):
        return True
    return False

print(is_triangle(0, 2, 3))