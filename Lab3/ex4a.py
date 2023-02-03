x = lambda a: a * 2
b = input()
for i in b:
    if i == " ":
        continue
    else:
        print(x(i))