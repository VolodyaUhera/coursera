class PayLips:
    def __init__(self, name,payment,amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
        
        
    def pay(self):
        self.payment = "yes"
        
    def status(self):
        if self.payment == "yes":
            return self.name + ' is paid' + str(self.amount)
        else:
            return self.name + ' is not paid yet'
        
        
nathan = PayLips("Nathan", "no", 1000)
rodger = PayLips("rodger", "no", 3000)

print(nathan.status(),"\n",rodger.status())

nathan.pay()

print(nathan.status(),"\n",rodger.status())
