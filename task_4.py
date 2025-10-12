def money_exchange(amount):
    ''' Задача 4. Размен денег '''
    denominations = [100, 50, 10, 5, 2, 1]
    result = {}
    for denom in denominations:
            count = amount // denom
            result[denom] = count
            amount %= denom

    return result

rubles = int(input("Введите сумму в рублях: "))
exchange = money_exchange(rubles)

print("Размен:")
for denom, count in exchange.items():
    print(f"{denom} руб.: {count}")
