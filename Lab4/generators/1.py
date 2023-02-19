n = int(input("Enter number: "))
def sqr():
    for i in range(1, n + 1):
        yield i ** 2
for i in sqr():
    print(i)
