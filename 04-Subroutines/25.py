n = ["Janek","Ania","Wojtek","Zosia"]

def jestImie(imie,imiona):
    print(f"Imiona: {','.join(str(x) for x in n)}")
    print(f"Imie: {imie}")
    print(f"Rezultat: imie {'zawarte jest' if imie in n else 'nie jest zawarte'} w wykazie imion")
    
name = 'Janek'
jestImie(name, n)
    