# book_assignment.py

# 1. Book class
class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            return copies_sold * self.price * 0.10
        elif copies_sold <= 1500:
            return (500 * self.price * 0.10) + \
                   ((copies_sold - 500) * self.price * 0.125)
        else:
            return (500 * self.price * 0.10) + \
                   (1000 * self.price * 0.125) + \
                   ((copies_sold - 1500) * self.price * 0.15)


# 2. EBook class (inherited)
class EBook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, value):
        self._ebook_format = value

    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        return base_royalty - (base_royalty * 0.12)


# 3. Driver code (very important for assignments)
if __name__ == "__main__":
    book = Book("Python Basics", "Prashant", "TechPress", 500)
    ebook = EBook("Python Basics", "Prashant", "TechPress", 500, "PDF")

    print("Book Royalty:", book.royalty(2000))
    print("EBook Royalty (after GST):", ebook.royalty(2000))
