res = {}
def for_tri(a, b, c):
        area =(b * c/2) / 2
        peri = a + b + c
        res["Площадь фигуры"] = area
        res["Периметр фигуры"] = peri
        print(res)
def for_squ(a, b):
        area = a ** 2
        peri = a * 4
        res["Площадь фигуры"] = area
        res["Периметр фигуры"] = peri
        print(res)
def for_rec(a, b):
        area = a * b
        peri = (a + b) * 2
        res["Площадь фигуры"] = area
        res["Периметр фигуры"] = peri
        print(res)
b = input()
if b.lower() == "rectangle":
    for_rec(int(input()), int(input()))
elif b.lower() == "square":
    for_squ(int(input()), int(input()))
elif b.lower() == "right triangle":
    for_tri(int(input()), int(input()), int(input()))
else:
    print("Введите правильную фигуру")