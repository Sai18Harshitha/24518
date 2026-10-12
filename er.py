
#create class
class biodata:
     founded = 1998
     #constractor
     def __init__ (self,name,age,salary,role,):
         self.name=name
         self.age=age
         self.salary=salary
         self.role=role
         self.company= "Wipro"
         
     def getpersonal(self):
        surname="murahari rao"
        print(f"employee name-{surname}.{self.name}")
    
     def getprofessional(self):
        print(f"company name-{self.company}")
        print(f"company founded in-{self.founded}") 
        
        
        
    #object
user1 = biodata("tulasi",80000,"SDE")
user2 = biodata("jessica",21,30000,"intern")

user1.getpersonal()
user2.getprofessional()