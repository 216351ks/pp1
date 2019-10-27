for i in range(3):
    if input('Podaj PIN: ') == '0805':
        print("PIN poprawny")
        break
    
    else:
        print('PIN niepoprawny')
    if i == 2:
        print('Karta zablokowana')