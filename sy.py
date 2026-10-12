#perent
class animal:
    def sound(self):
        print("animal is making some sound..")
        
    def flying(self):
        print("it is flying")
#child
class dog(animal):
    def sound(self):
        print("shabana is a dog...")
    def search(self):
        print("dog finds theif by sniffing nose")
    
    def eat(self):
        print("shabana is eating mell")
        
rita=dog()
rita.sound()
rita.flying()
rita.search()
rita.eat()
