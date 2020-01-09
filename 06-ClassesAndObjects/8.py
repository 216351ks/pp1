class University:
    
    def __init__(self):
        self.name = 'UEK'
    
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name
u1 = University()
u1.set_name('AGH')
u1.print_name()
