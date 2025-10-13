def calculate_bill(minutes_used, sms_used, data_used_mb):
    ''' Задача 12. Счет за телефон '''
    base_minutes = 60
    base_sms = 30
    base_data_mb = 1024  # 1 ГБ = 1024 МБ
    base_price = 24.99

    # Стоимость дополнительных услуг
    extra_minute_price = 0.89
    extra_sms_price = 0.59
    extra_data_price = 0.79
    tax_rate = 0.02

    # Расчёт перерасхода
    extra_minutes = max(0, minutes_used - base_minutes)
    extra_sms = max(0, sms_used - base_sms)
    extra_data = max(0, data_used_mb - base_data_mb)

    # Стоимость дополнительных услуг
    extra_minutes_cost = extra_minutes * extra_minute_price
    extra_sms_cost = extra_sms * extra_sms_price
    extra_data_cost = extra_data * extra_data_price

    # Общая сумма до налога
    subtotal = base_price + extra_minutes_cost + extra_sms_cost + extra_data_cost

    # Налог
    tax = subtotal * tax_rate

    # Итоговая сумма
    total = subtotal + tax

    # Вывод
    print(f"Базовая сумма тарификации: {base_price:.2f} руб.")
    if extra_minutes > 0:
        print(f"Дополнительные минуты: {extra_minutes} мин. — {extra_minutes_cost:.2f} руб.")
    if extra_sms > 0:
        print(f"Дополнительные SMS: {extra_sms} шт. — {extra_sms_cost:.2f} руб.")
    if extra_data > 0:
        print(f"Дополнительный интернет: {extra_data} МБ — {extra_data_cost:.2f} руб.")
    print(f"Налог (2%): {tax:.2f} руб.")
    print(f"Итоговая сумма к оплате: {total:.2f} руб.")

# Ввод данных
minutes = int(input("Введите количество использованных минут: "))
sms = int(input("Введите количество отправленных SMS: "))
data_mb = int(input("Введите объём использованного интернет-трафика (в МБ): "))

# Расчёт и вывод
calculate_bill(minutes, sms, data_mb)
