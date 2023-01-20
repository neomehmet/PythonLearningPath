# polymorphism

class Banana():
    def __init__(self,isim):
        self.isim = isim
        print("Banana init")
    def calori(self):
        return 250


class Apple():
    def __init__(self, isim):
        self.isim = isim
        print("apple init")
    def calori(self):
        return 150

apple1 = Apple("kastamonu")
banan1 = Banana("Anamur")

appleCalor = apple1.calori()
bananaCalor = banan1.calori()
print(appleCalor)
print(bananaCalor)
print("\n")
fruitList = [apple1,banan1]
for fruit in fruitList:
    print(fruit.calori())
    print("\n")

def takeinfo(fruit):
    print("\n exampe of polymorphism : " + str(fruit.calori()))

takeinfo(banan1)