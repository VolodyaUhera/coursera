animal = 'boooooooooi'
def d():
    animal = 'elephant'
    def e():
        global animal
        animal = 'girafe'
        print('indisde nested function: ' + animal)

    print('Before calling function: ' + animal)
    e()
    print('After ' + animal)

# animal = 'camel'
d()
print("Global animal: "+ animal)