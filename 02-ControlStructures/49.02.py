n= int(input("POdaj numer dnia tygodnia: "))
dni_tyg = ["PN","WT","ŚR","CZW","PT","SB","ND"]
print(f'| {" | ".join(dni_tyg)} |')

for y in range(1 - n,31):
    if y > 0:
        print(f'| {y:2} ', end='')
        if not (y + n) %7:
            print('|')
            
    else:
        print(f'|    ',end='')