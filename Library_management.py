class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f" {self.title} by {self.author} ({'Available' if self.is_available else 'Issued'})"
    

class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,title,author):
        book = Book(title,author)
        self.book.append(book)
        print(f'your book {title} added successfully')

    def remove_book(self,title):
        for book in self.book:
            if book.title == title:
                self.book.remove(book)
                print(f"your book {title} is removed successfully")
                return
        print(f"your book {title} is not found in library!")

    def display_book(self):
        if not self.book:
            print('no book is available in library')
        else:
            for book in self.book:
                print(book)
    
    def issue_book(self,title):
        for book in self.book:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"your book {title} is issued")
                else:
                    print(f"your book {title} is already issued")
                return
        print(f"book {title} is not found in library")

    def return_book(self,title):
        for book in self.book:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"book {title} has been returned.")
                else:
                    print(f"book {title} has not issued.")
                return
        print(f'Book {title} not found in library database!')


if __name__ == '__main__':
    c1 = Library()
    c1.add_book('python book','aditya')
    c1.add_book('java','aditya')
    c1.add_book('c++ book','aditya')
    c1.display_book()
    c1.issue_book('java')
    c1.display_book()
    c1.return_book('java')
    c1.display_book()
    c1.remove_book('c++ book')
    c1.display_book()

                

            

            