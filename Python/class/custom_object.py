class MyFirstClass:
    print("who wrote this")
    index = "Author-Book"
    
    def hand_list(self, philosopher , book):
        self.philosopher = philosopher
        self.book = book
        
        print(MyFirstClass.index)
        print(book + " wrote the book: "+ philosopher)
        
whodunnit = MyFirstClass()

whodunnit.hand_list("sun Tzu", "The Art of War")