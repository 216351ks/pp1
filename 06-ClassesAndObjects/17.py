def Ulamek():
    
    def __init__(self):
        pass
        
    def create_ulamek(self, licznik, mianownik):
        if mianownik == 0:
            print('Mianownik nie może być równy 0')
            
        else:
            self.licznik = licznik
            self.mianownik = mianownik
        
    def show_ulamek(self):
        print(f'Ułamek: {self.licznik}/{self.mianownik}')
        
ul = Ulamek()

ul.create_ulamek(1, 2)
ul.show_ulamek()
print('----')
ul.create_ulamek(12, 21)
ul.show_ulamek
        

        
    