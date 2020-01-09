class Student:
    number = 100000
    uni = 'UEK Kraków'
    def __init__(self, name, surname, field):
        Student.number +=1
        self.album_number = Student.number
        self.name = name
        self.surname = surname
        self.field = field
        
    def __str__(self):
        return(f"{self.name} {self.surname} ({self.album_number}), {self.field}, {Student.uni}")
    
s1 = Student('Kacper','Siwiec','Informatyka Stosowana')
s2 = Student('Kuba','Duke', 'Zarzadzanie')
print(s1)
print(s2)
        
    