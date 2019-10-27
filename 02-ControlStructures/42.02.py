a = int(input('Podaj dowolną liczbę: '))
b = int(input('Podaj dowolną liczbę: '))


try:
    
    print(f'Wynik:   {a/b}')
    
except ZeroDivisionError:
    print('Dzielenie przez 0!!!')
