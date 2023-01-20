

class Fruit():

    def __init__(self,isim,calori):
        self.isim = isim
        self.calori = calori

    def __str__(self): # this like function overloading friend function kind of
        return f"{self.isim}, {self.calori}"
    def __len__(self):
        return self.calori
    #where to find this methods, you search google on "special methods in python"
    # or magic methods - special methods
banana = Fruit("banana",240)

print(banana)
print(len(banana))





