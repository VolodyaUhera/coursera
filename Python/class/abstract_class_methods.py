from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass


class Donation(Employee):
    def donate(self):
        self.a = int(input("How much would you like to donate: "))
        return self.a

    def __str__(self):
        return f"{self.a} + donated "


class Donation2(Employee):
    def donate(self):
        return 100


amounts = []

john = Donation()
j = john.donate()
print('jhon')
print(john)
amounts.append(j)


peter = Donation()
p = peter.donate()
print('peter')
amounts.append(p)

bob = Donation2()
b = bob.donate()
amounts.append(b)

print(amounts)
print(sum(amounts))
print(Donation.mro())
print(help(Donation))