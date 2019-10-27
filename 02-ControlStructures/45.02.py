lim = int(input("Podaj Liczbę:"))
tab=[]
b = 2
while len(tab) < lim:
    for a in range(2,b):
        if(b % a) == 0:
            break
        
        else:
            tab.append(b)
        b += 1
        print('Liczby pierwsze: ')
        print(tab)