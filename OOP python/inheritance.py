class Animal():
    def __init__(self,type, location):
        self.type = type
        self.location = location
    def exampleFunc(self):
        print(" loves from ISTANBUL\n  loves from ISTANBUL  \n<3 <3  ATATURK <3 <3  father of Turks")
    def exampleOverRide(self):
        print("animal function")

class Fish(Animal):
    def __init__(self,type, location ,kg):
        self.kg = kg
        Animal.__init__(self, type, location) ## takes from Animal CLass
        print(f"Fish init, \n {self.type} is Type, {self.kg} is weight, {self.location} is where they lives")
  #  def exampleOverRide(self): # delete # in this line  and after run code to see how override runs in python
   #     print("fish function")

myFish = Fish( "jaws" , "pacific", 100)
myFish.exampleFunc()  # i call even functions of Animal class,
## it is one of basic example the inheritance to show  parent-child relation at OOP programming

myFishTwo = Fish("tuna","arctic",300)
myFish.exampleOverRide()