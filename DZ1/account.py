def calculate_income(rate, cache, month):
    if cache <= 0:
        return 0

    for i in range(1, month + 1):
        cache = round(cache + cache * rate / 100 / 12, 2)
    return cache


def main():
    rate =10
    cache = 100000
    period = 12

    result = calculate_income(rate, cache, period)
    print("Параметры счёта:\n", "Сумма:", cache,"\n", "Ставка: ", rate, "\n", "Период", period, "Сумма на счёте в конце периода:", result)

if __name__=="__main__":
    main()
