def format_fio(fio):
    parts = fio.split(" ")
    if len(parts) != 3:
        print("wrong format of fio")
    first_part, second_part, third_part = parts
    return f"{first_part} {second_part[0]}. {third_part[0]}."

fio = input("введите ФИО:")
print(format_fio(fio))