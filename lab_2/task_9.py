#9.    Напишите программу, которая считает количество различных символов в строке.
str_1 = "jlsfkfslt"
str_2 = ""
count = 0
for ch in str_1:
    if ch not in str_2:
        count +=1
        str_2 += ch
    elif count>0:
        count -=1
print(count)