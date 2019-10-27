a = int (input("Podaj wymiary pierwszego boku:"))
b = int (input("Podaj wymiary drugiego boku:"))
c = int(input("Podaj wymieray trzeciego boku:"))


f= ((1/2*(a+b+c))*(1/2*(a+b+c)-a)+(1/2*(a+b+c)-b)+(1/2*(a+b+c)-c))**1/2
print(f" Pole trójkąta wynosi: {f}")