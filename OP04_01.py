def sum_range(start, end):
    summa = 0
    for i in range(start, end + 1):
        summa += i
    return summa

st = int(input("введите начальное значение "))
en = int(input("введите коненчное значение "))
if st < en:
    total=sum_range(st, en)
else:
    total = sum_range(en, st)
print(f"Сумма: {total}")

