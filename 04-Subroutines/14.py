tab = [15,38,23,7,14]

def wystepuje(liczba, tablica):
    print(f'Liczba: {liczba}')
    print(f"Tablica: {','.join(str(x)for x in tab)}")
    print(f"Podana liczba {'występuje' if liczba in tablica else 'nie występuje'} w tablicy")
wystepuje(23,tab)   
    