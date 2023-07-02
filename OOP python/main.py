class Vehicle:
    pass

xinstance = Vehicle()

Vehicle.classAttribute = "class Attribute added"
xinstance.instanceAttribute = "instance Attribute added"
 # class no instance attribute but obj has 

print( Vehicle.classAttribute  )
print( xinstance.instanceAttribute )