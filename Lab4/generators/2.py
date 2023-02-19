n = int(input("Введите число: "))
def ev():
    for even in range(0, n+1, 2):
        yield even
list = []
for i in ev():
    list.append(str(i))
print(",".join(list))