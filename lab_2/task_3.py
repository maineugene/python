#3.    Создайте словарь с именами студентов и их возрастами. Найдите самого старшего студента.
students = {"Evgeniy" : 18,"Alexandr" : 20, "Pavel" : 21}
max_age = max(students.values())
for key,value in students.items():
    if value == max_age:
        print(f"самый старший студент:{key}, его возраст:{value}")
        break
