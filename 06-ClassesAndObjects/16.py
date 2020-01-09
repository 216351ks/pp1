from ebookclass import Ebook

book = Ebook('Ślepnąc od świateł', 'Jakub Żulczyk', 520)

book.open_book()
book.show_status()
for _ in range(325):
    book.read_next()
for _ in range(64):
    book.read_prev()
book.show_status()
book.close_book()
book.read_next

