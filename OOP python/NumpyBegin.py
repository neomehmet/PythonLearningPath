import numpy as np
#linspace, arange,

mylist = [20,30,40]
print(type(mylist))

myNpArr = np.array(mylist)
print(type(myNpArr))

matrix = [ [1,2,3],[4,5,6],[7,8,9]]

npMatrix = np.array(matrix)
print( npMatrix )
print( matrix )

# arange function : oto list creates
temp = np.arange(0,10)
print(temp)

temp = np.arange(0,20,1.5) #start, stop, step
print(temp)

# zeros empty list
print( np.zeros((3,3)) )
print( np.ones(7) )

#linspace : create array with equals steps away
temp = np.linspace(0,20,6)
print(temp)  # star, stop, interspace number
temp = np.linspace(0,5,7)
print(temp)  # star, stop, interspace number

# eye : create unit(identity matrix
print(np.eye(3), np.eye(5))



