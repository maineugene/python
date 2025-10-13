#4.   Напишите программу, которая находит сумму всех цифр числа N.
number = input("enter:")
sum = sum(int(digit) for digit in number if digit.isdigit())
print(sum)