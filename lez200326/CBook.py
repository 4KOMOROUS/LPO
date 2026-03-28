# definizione e uso della classe CBook

class CBook():
    def __init__(self, title, autor, editor, isbn, release_year, price): # metodo costruttore della classe
        self.title = title
        self.autor = autor
        self.editor = editor
        self.isbn = isbn
        self.release_year = release_year
        self.price = price

    # uso di self -> self rappresenta l'istanza corrente della classe (es. my_book)

    # metodo che stampa il titolo  e il prezzo dell'oggetto libro
    def print_data(self):
        print(f"title:{self.title}\nprice: {self.price}")

    # metodo per calcolare l'età del libro (privato -> inizia col "_")
    def _calc_book_age(self, this_year):
        book_age = this_year - self.release_year
        return book_age
    
    # metodo privato per calcolare lo sconto in base all'età del libro (se maggiore di 5 anni -> 5% di sconto)
    def _calc_discount(self, this_year):
        if(self._calc_book_age(this_year) > 5):
            discount = self.price * 5 / 100
        else:
            discount = 0
        return discount

t = input("type the title of the book: ")
a = input("type the name of the autor: ")
e = input("type the name of the editor: ")
i = int(input("type the isbn code: "))
r = int(input("type the release year: "))
p = float(input("type the price: "))


my_book = CBook(t, a, e, i, r, p)  # creazione istanza della classe CBook
my_book.print_data()
print(f"discount: {my_book._calc_discount(2026)}$")
print(hasattr(my_book, "editor"))  # verifica se l'oggetto possiede un determinato attributo (restituirà True) 