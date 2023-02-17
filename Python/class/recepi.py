class Recepi():
    # def __new__(cls: type[Self]) -> Self:
    #     pass

    # def __init__(self) -> None:
    #     pass

    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def content(self):
        print("The " + str(self.dish) + " has "+ str(self.items) + \
            ' and time '+ str(self.time) + ' min to prepare')


pizza = Recepi('Pizza', ['chees','bread','tomato'], 45)
pasta = Recepi('paste', ['penne','sauce'], 45)

print(pizza.content())
print(pasta.content())
