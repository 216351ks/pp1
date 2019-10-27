x = 0
s = 0
while True:
    z=int(input('Podaj liczbę :'))
    if z == 0:
        srednia= s/x
        break
    
    x +=1
    s +=z
    print(f' REZULTAT: Liczb:{x}, Suma={s}, Średnia={sredna}')
    