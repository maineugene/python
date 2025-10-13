def gas_amount(pressure, temperature, volume):
    ''' Задача 6. Уравнение состояния идеального газа '''
    R = 8.31
    return pressure * volume / (R * temperature)
# pv = nRT n=pv/RT
pressure , temperature, volume = float(input("введите давление(в Паскалях):")),float(input("введите температуру (в Кельвинах):")), float(input("введите объем(в м^3):"))
print("количество газа:",gas_amount(pressure , temperature, volume)," моль")

