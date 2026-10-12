

class Interest:
    def __init__(self, p, t):
        self.p =p
        self.t = t
        self.R = 0.18

    def calculate(self):                          
        amount = (self.p * self.R * self.t) / 100
        return f"Amount = {amount}"


loan1 = Interest(2356.45, 2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
print(loan1.calculate())
