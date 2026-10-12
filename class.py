#creation of the class
class operation:
    def greet(self):
        print("welcome to operation")
        
        
    def addnum(self,a,b):
        return f"sum={a+b}"
    
    
    def sub(self,a,b):
        return f"sub={a-b}"
    
    # creating object
    
Tulasi = operation()
Tulasi.greet()
print(Tulasi.addnum(12,90))
print(Tulasi.sub(34,56))


 #calling function       
operation.greet()
operation.addnum(2,4)
print(operation.sub(625,50))