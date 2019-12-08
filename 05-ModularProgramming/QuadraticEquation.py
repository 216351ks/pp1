def Wspolczynnik():
    a = int(input("Podaj współczynnik a: "))
    b = int(input("Podaj współczynnik b: "))
    c = int(input("Podaj współczynnik c: "))
    
    print(f"Równanie kwadratowe : {a}x2 + {b}x + {c}")
    return [a, b ,c]
    
    
def Delta(parametry):
    if parametry[0] == 0:
        raise ZeroDivisionError
    else:
        delta = parametry[1]**2 - 4*parametry[0]*parametry[2]
        return delta
    
def Pierwiastki(parametry):
    import math
    
    delta = Delta(parametry)
    
    if delta < 0:
        return None
    elif delta == 0:        
        x0 = ((-1) * parametry[1]) / (2*parametry[0])
        return x0
    else:
        x1 = ((-1) * parametry[1] - math.sqrt(delta)) / (2*parametry[0])
        x2 = ((-1) * parametry[1] - math.sqrt(delta)) / (2*parametry[0])
        return[x1,x2]

def wyswietlPierwiastki(tablica):
    
    if tablica == None:
        print(' ')
        
    elif isinstance(tablica, (float,int)):
        print(f'Pierwiastek równania: x0 = {tablica}')
        
    else:
        print(f'Pierwiastki równania są równe: x1 = {tablica[0]}, x2 = {tablica[1]}')
