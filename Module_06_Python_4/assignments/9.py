class Herbivore():
    def __init__(self, herbivoreName):
        self.herbivoreName = herbivoreName
    def eat(self):
        return(f"{self.herbivoreName} is Eating Grass...")

class Carnivore():
    def __init__(self, carnivoreName):
        self.carnivoreName = carnivoreName
    def eat(self):
        return(f"{self.carnivoreName} is Eating Meat ...")
        
class Omnivore():
    def __init__(self, omnivoreName):
        self.omnivoreName = omnivoreName
    def eat(self):
        return(f"{self.omnivoreName} is Eating both Grass and Meat ...")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        super().__init__(name)   # Sets herbivoreName = name
        Carnivore.__init__(self, "Carnivore " + str(name)) # Sets carnivoreName = Canivore name
        Omnivore.__init__(self, "Omnivore " + str(name)) # Sets omnivoreName = Omnivore name   
    
    def eat(self):
        return f"{super().eat()}\n{Carnivore.eat(self)}\n{Omnivore.eat(self)}"
    
teddy = Bear("Teddy Bear")
print(teddy.eat())