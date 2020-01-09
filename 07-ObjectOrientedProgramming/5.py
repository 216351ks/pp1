class Song:
    def __init__(self, author, title, album, year):
        self.author = author
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
         return (f' Wykonawca : {self.author} \n Utwór : {self.title} \n Album : {self.album} \n Rok: {self.year}')
s1 = Song('Dawid Podsiadło','Nie ma fal','Małomiasteczkowy',2018)
print(s1)
    
    
    



