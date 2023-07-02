class Vehicle:
    pass

bmw = Vehicle()
ford = Vehicle()

# adding attributes to the class
Vehicle.Year = "2019"

#adding attributes to the object
bmw.Owner = "john"

#adding attributes to the object
ford.Gear = "manual"

print(bmw.Owner)

print(ford.Gear)    
print(ford.Year, bmw.Year)