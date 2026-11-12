class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Book unavailable")

    def return_book(self):
        self.available = True
        print("Book returned")

    def display(self):
        print("Book:", self.name)
        print("Available:", self.available)


b = Book("Python")
b.display()
b.issue()
b.display()
b.return_book()
b.display()