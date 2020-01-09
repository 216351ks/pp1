class Ebook():
    
    def __init__(self, title, author, page_num):
        self.title = title
        self.author = author
        self.page_num = page_num
        self.is_open = False
        self.current_page = 1
        
    def open_book(self):
        self.is_open = True
        
    def close_book(self):
        self.is_open = False
        
    def show_status(self):
        print(f"Tytuł: {self.title}\nAutor: {self.author}\nStrona: {self.page_num}\nBieżąca strona: {self.current_page}")
        
    def read_next(self):
        if self.is_open:
            if self.current_page < self.page_num:
                self.current_page += 1
                
        else:
            print("Książka jest zamknięta")
            
    def read_prev(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                
        else:
            print("Książka zamknięta")
            
            
        
    
    