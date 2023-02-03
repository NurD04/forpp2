def calculator(operation, num1, num2):
    operations = {
        'add': lambda x, y: x + y,        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,        'divide': lambda x, y: x / y,
        'degree': lambda x, y: x ** y
    }
    return operations[operation](num1, num2)
for i in range(1):
    a = int(input())
    b = int(input())
    c = input("Выберите оператор: + \n - \n * \n / \n ** \n ")
    if c == '+':
         print(calculator('add', a, b))
    elif c == '-':
         print(calculator('subtract', a, b))
    elif c == '*':
         print(calculator('multiply', a, b))
    elif c == '/':
         print(calculator('divide', a, b))
    else:
        print(calculator('degree', a, b))