def square(a):
    sq = []
    sq.append(a * 4)
    sq.append(a ** 2)
    sq.append((2 * a ** 2) ** (0.5))
    return sq

aa = int(input(" Введите сторону кадрата "))
res = square(aa)
print(f" Периметр: {res[0]}, Площадь: {res[1]}, Диагональ: {res[2]}")