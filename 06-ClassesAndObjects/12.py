class TV:
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    
    def show_status(self):
        if self.is_on:
            print(f'Telewizor jest włączony, kanał {self.channel_no}')
        else:
            print('Telewizor wyłączony')
            
tv = TV()
tv.show_status()
tv.on()
tv.show_status()
tv.set_channel(input('zmień kanał na: '))
tv.show_status()
tv.off()
tv.show_status()