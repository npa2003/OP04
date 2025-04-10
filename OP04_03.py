bank1 = lambda sum, years: sum * (1 + 0.1) ** years

x1 = int(input(" Внесённая сумма: "))
x2 = int(input(" Кол-во лет: "))
print("Сумма в конце срока", bank1(x1, x2))
