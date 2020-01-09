class University:
    def __init__(self,):
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
    
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_fullname(self,new_name):
        self.fullname = new_name
    
    def print_fullname(self):
        print(self.fullname)
u1 = University()

u1.print_fullname()
u1.set_fullname(input('wprowadź nazwę: '))
u1.print_fullname()