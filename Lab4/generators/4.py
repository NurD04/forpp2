a = int(input("Выберите начало диапазона: "))
b = int(input("Выберите конец диапазона: "))
def squ():
    for i in range(a, b + 1):
        yield i ** 2
list = []
for i in squ():
    list.append(str(i))
print(",".join(list))
