class Publication:
    
    def __init__(self, name):
        self.name = name

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_mags(self): 
        print(f"Magazine name is: {self.name}, Chief editor is: {self.chief_editor}")
        

class Book(Publication):
    
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)
        
    def print_books(self):
        print(f"name is: {self.name}, Author is: {self.author}, page count is: {self.page_count}")

mags =[]      
books = []

books.append(Book(f"Compartment No. 6" ,"Rosa Liksom", 192 ))

mags.append(Magazine("Donald Duck","Aki Hyyppä"))
for m in mags:
    m.print_mags()
for b in books:
    b.print_books()