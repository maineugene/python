def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part.startswith('0'):
            return False  # ведущий ноль недопустим
        num = int(part)
        if not (0 <= num <= 255):
            return False
    return True

ip = input("Введите IP-адрес: ")
if is_valid_ip(ip):
    print("Корректный IP-адрес")
else:
    print("Некорректный IP-адрес")
