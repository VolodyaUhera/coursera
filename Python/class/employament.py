class Employyes:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last
        
        
class Supervisors(Employyes):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employyes):
    def leave_request(self, days):
        return "may i atake a leave for " + str(days) + " days"
    

adrian = Supervisors("adrian", "A", "apple")

emily = Chefs("Emily", "E")
john = Chefs("john", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)