def palindrom(s):
    s_clean = s.replace(" ", "").lower()
    return s_clean == s_clean[::-1]
s = input("Введите строку: ")
if palindrom(s):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
