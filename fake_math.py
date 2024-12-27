def divide(first , second):
    if second == 0:
        res = 'Ошибка'
    else:
        res = first / second
    return res

a = divide(4 , 0)
print(a)
