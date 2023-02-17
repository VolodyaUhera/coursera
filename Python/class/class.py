class Alpha:

    def __init__(self):
        self._a = 2.  # Protected member ‘a’ #accesed by class and subclassses #PROTECTED
        self.__b = 2.  # Private member ‘b’ #only be accessed from within the Alpha class #PRIVATE
        

class MyClass:
    a = 5
    print('hello')
    
    def hello(self):
        print('hello world')

myclass = MyClass()
print(myclass.a)
print(myclass.hello())