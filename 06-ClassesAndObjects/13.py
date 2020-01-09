class TV:
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel = []
        
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
    
    def set_channels(self, channels_list):
        self.channels = channels_list
        
    def show_channels(self):
        print(self.channels)
        
    def show_status(self):
        if self.is_on:
            print(f'Kanały: {self.channels[self.channel_no - 1]}')
            print(f'Telewizor jest włączony, kanał {self.channel_no}')
        else:
            print('Telewizor wyłączony')

channels = ['TVP1','Polsat','TVN','BBC']            
tv = TV()
tv.show_status()
tv.on()
tv.set_channels(channels)
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.off()
tv.show_status()