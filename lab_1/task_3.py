def password_check(password):
    #Задача 3. Проверка пароля
    if len(password) <16 :
        return "слишком маленький"
    elif password.isalpha() or password.isdigit():
        return "слабый пароль"
    else:
        return "надежный пароль"

password = input("enter password:")
print(password_check(password))