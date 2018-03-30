usd=57
euro=60
phynt=79

money=int(input('Введите сумму, которую вы хотите обменять:'))
currency= int(input('Укажите код валюты(Доллары-400, Евро-401, Фунты-402):'))

if currency==400:
    cache=round(money/usd, 2)
    print('Валюта: Доллары США')
elif currency==401:
    cache = round(money / euro, 2)
    print('Валюта: Евро')
elif currency==402:
    cache = round(money / phynt, 2)
    print('Валюта: Фунты')
else:
    cache=0
    print('Неизвестная валюта')

print ('К получению:', cache)
