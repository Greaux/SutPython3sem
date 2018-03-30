import account
import converter

def main():
    rate = int(input('Введите процентную ставку:'))
    money = int(input('Введите сумму:'))
    period = int(input('Введите период ведения счета в месяцах:'))

    usd = 57
    euro = 60
    phynt = 79

    currency = int(input('Укажите код валюты(Доллары-400, Евро-401, Фунты-402):'))

    if currency == 400:
        cache = round(money / usd, 2)
        print('Валюта: Доллары США')
    elif currency == 401:
        cache = round(money / euro, 2)
        print('Валюта: Евро')
    elif currency == 402:
        cache = round(money / phynt, 2)
        print('Валюта: Фунты')
    else:
        cache = 0
        print('Неизвестная валюта')

    print('Внесено в банк:', cache)

    result= account.calculate_income(rate,cache,period)
    print('Параметры счета:\n', 'Сумма:', cache, '\n', 'Ставка:', rate, '\n', 'Период:', period, '\n', 'Сумма на счете в конце периода:', result)

if __name__ == "__main__":
    main()
