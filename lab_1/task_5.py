def check_magic_number(number):
    ''' Задача 5. Магическое число '''
    if number % 7 == 0:
        return "Магическое число!"
    else:
        digit_sum = 0
        number = abs(number)
        for digit in str(number):
            digit_sum += int(digit)
        return f"Сумма цифр:{digit_sum}"
user_input = int(input("Введите число: "))
print(check_magic_number(user_input))
