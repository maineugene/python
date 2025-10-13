def operations(a,b):
    ''' Задача 10. Арифметика '''
    print(f"сумма:{a+b}")
    print(f"разность:{a-b}")
    print(f"произведение:{a * b}")
    print(f"частное:{a / b}")
    print(f"остаток от деления:{a % b}")
    print(f"возведение в степень:{a ** b}")

a,b = int(input("enter a:")),int(input("enter b:"))
operations(a,b)