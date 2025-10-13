#вариант 3
#1.    Напишите программу, которая выводит все простые числа от 1 до N.
import math
def task(n):
    simple = []
    for i in range (2,n):
        is_simple = True
        for j in range(2,int(math.sqrt(n)+1)):
            if i % j == 0:
                is_simple = False
                break
        if is_simple == True:
            simple.append(i)
    return simple

n = int(input("enter a number:"))
print(task(n))
