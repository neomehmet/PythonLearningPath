#class
name = "No Name"
age = int(2000)
job = "No Job"
class Hero():
    def __init__(self,name,age,job):
        print(" init called")
        self.name = name
        self.age = age
        self.job = job

superman = Hero("Clark Kent",30,"Journalist");
print(superman.name, superman.age, superman.job)

conqueror = Hero("Mehmet Ottoman",21,"Politician")
print(conqueror.name, conqueror.age, conqueror.job)

# methods #
class human():
    def __init__(self, name, age, job):
        print(" human init called")
        self.name = name
        self.age = age
        self.job = job
    def exampleMethod(self):
        print("human example method called")
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
        print(f"age update  : {self.age}")

me = human("Mehmet",25,"student")
#me.exampleMethod()

name_x = me.getName()
print(name_x)

me.setAge(27)
print(me.age)

#default args

class Dog():
    def __init__(self, age = 1 ): #this the default args
        self.age = age
    def getAge(self):
        return self.age


myDog = Dog(5)
yourDog = Dog()

print(f"my dog age : {myDog.age}, your dog age : {yourDog.age}")


class Animal():
    def __init__(self,type, location):
        self.type = type
        self.location = location

class Fish(Animal):
    def __init__(self,type, location ,kg):
        self.kg = kg
        Animal.__init__(self, type, location)
        print(f"Fish init, \n {self.type} is Type, {self.kg} is weight, {self.location} is where they lives")

myFish = Fish( "jaws" , "pacific", 100)








