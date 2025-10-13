#вариант 6
#2.    Дан список чисел. Найдите сумму чисел, кратных 3.
def multiples_of_3(numbers):
    sum = 0
    for i in numbers:
        if i % 3 == 0:
            sum += i
    return sum

numbers = input("введите числа через пробел:").split(" ")
numbers = [int(num) for num in numbers if num != '']
print(multiples_of_3(numbers))

