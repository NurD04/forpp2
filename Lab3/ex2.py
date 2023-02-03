# we can do also so
# x = input()
# print(x[ : :-1])
x = input()
y = ""
z = ""
if x[0] != '-':
    if x[len(x) - 1] == '0':
        for i in range(len(x)):
            if len(x) - (i + 1) == len(x) - 1:
                continue
            else:
                y += x[len(x) - (i + 1)]
        print(y)
    else:
        for i in range(len(x)):
            y += x[len(x) - (i + 1)]
        print(y)
else:
    y +=x[0]
    if x[len(x) - 1] == '0':
        for i in range(len(x)):
            if len(x) - (i + 1) == len(x) - 1:
                continue
            else:
                y += x[len(x) - (i + 1)]
        print(y)
    else:
        for i in range(len(x)):
             if len(x) - (i + 1) == 0:
                 continue
             else:
                  y += x[len(x) - (i + 1)]
        print(y)
