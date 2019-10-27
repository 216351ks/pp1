waga = int(input("Podaj swoją wagę w kilogramach:"))
wzrost = float(input(" Podaj swój wzrost w m:"))
BMI = waga / (wzrost**2)
print(f' Wskaxnik BMI: {BMI}', 'waga prawidłowa' if 25>BMI>18.5 else 'waga nieprawidłowa'  )
           