#5.   Дан список строк. Выведите те, которые начинаются с заглавной буквы.
string_list = ["Hello ","!", "world","!","Василий"]
for string in string_list:
    if string[0].isupper():
        print(string)