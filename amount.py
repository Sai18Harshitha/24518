

class intrest:
    def __init__ (self,p,t):
        self.p=p
        self.t=t
        self.R=0.18
        
    def calculate(self):
        Amount = (self.p*self.r*self.R)/100
        return f"Amount={Amount}"
loan1=intrest(2356.45)
print(loan1.calculate())
