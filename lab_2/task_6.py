#6.    Напишите программу, которая проверяет, содержится ли введённое слово в списке строк.
strings = ["hello", "Ivan", "345"]
word = input("enter a word:")
if word in strings:
    print("содержится")
else:
    print("не содержится")
