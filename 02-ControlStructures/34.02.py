
#wiek i płeć na podstawie numeru pesel na rok 2018

b=input('Podaj swój numer PESEL:')

print(f"Płeć: {'mężczyzna' if int(b[-2]) %2 else 'kobieta'}")

print(f'Wiek: {118 - int(b[:2])}')