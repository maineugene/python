def palindrom(s):
    s_clean = s.replace(" ", "").lower()
    if s_clean == s_clean[::-1]:
        return True
    else:
        return False
s = input("Введите строку: ")
if palindrom(s):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
