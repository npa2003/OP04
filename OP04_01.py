def sum_range(start, end):
    summa = 0
    for i in range(start, end + 1):
        summa += i
    return summa

st = int(input("введите начальное значение "))
en = int(input("введите коненчное значение "))
total=sum_range(st, en)
print(f"Сумма: {total}")

