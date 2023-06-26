'''Решение задачи _Playing with digits_
Solution of task _Playing with digits_
'''
def dig_pow(n, p):
    pr = n
    len_n = len(str(pr))
    list_ns = []
    for i in range(len_n):
        o = pr%10
        if pr > round(pr/10):
            pr = int(pr/10)
        else:
            pr = round(pr/10)
        list_ns = [o] + list_ns
    sum = 0
    for i in range(len(list_ns)):
        list_ns[i] = pow(list_ns[i], p + i)
        sum = sum + list_ns[i]
    if sum % n == 0:
        return int(sum/n)
    return -1

'Преобразует входящее число в список цифр, из которого оно состоит'
def funx_c(n):
    'Количество цифр в числе'
    len_n = len(str(n))
    'Инициализация пустого списка'
    list_ns = []
    'Цикл для заполнения списка цифрами'
    for i in range(len_n):
        "Самую правую (наименьшую) цифру"
        o = n%10 
        "Проверяем следующую цифру на корректность определения"
        if n > round(n/10):
            "Если полученное больше, то используем другую функцию"
            n = int(n/10)
        else:
            "Если проблем нет, то оставляем округление"
            n = round(n/10)
            "Добавляем в начало списка новую цифру, порядок как в числе"
        list_ns = [o] + list_ns
    return list_ns

"Выводит (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) "
def polinom_listn(list_ns, p):
    sum = 0
    "Присваивает каждому элементу списка значение его в степени"
    for i in range(len(list_ns)):
        "Степень зависит от вводимого числа, но след. на 1 больше предыд."
        list_ns[i] = pow(list_ns[i], p + i)
        "Сумма всех полученных значений списка"
        sum = sum + list_ns[i]
    return sum

"Проверка числа k такого = (a^p+b^(p+1)+c^(p+2)+d^(p+3)+...)=k*n"
def sum_check(n, p, sum):
    "Еcли число делится нацело, то число k сущестует"
    if sum%n == 0:
        k = int(sum/n)
    else: 
        "Если нет, то выводим -1"
        k = -1
    return k

print(sum_check(46288, 3, polinom_listn(funx_c(46288), 3)))
print(dig_pow(46288, 3))