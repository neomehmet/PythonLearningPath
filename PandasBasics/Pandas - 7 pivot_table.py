import numpy as np
import pandas as pd

#query
data = { "name" : ["adam","bob","charles","david"],
         "department" : ["software","law","marketing","software"],
         "salary" : [100,600,300,150]
         }

dFrame = pd.DataFrame(data)
print(dFrame)
print(dFrame["department"])
print( dFrame["department"].unique() ) # get one each one
print(dFrame["department"].nunique()  ) # number uniq
print( dFrame["department"].value_counts() ) #

def netSalary(salary):
    return salary * 0.5
print(" get half of salary")
halfSalry = dFrame["salary"].apply(netSalary)
print(halfSalry)
print( dFrame.isnull() ) # null value control if there is null so shown below true

# pivot table
newData = {"char class" : ["simpson","simpson","south park","south park"],
           "char name" : ["homer", "bart", "cartman","kenny"],
           "char age" : [50,20,9,10]
           }
# we gonna pivot, like multi index
charDF = pd.DataFrame(newData)
print(charDF)

pivot = charDF.pivot_table(values="char age", index=["char class","char name"] )
print(pivot) # if there is the value line same values more than one line, pivot table get the mean
# if you dont get mean using pivot table
# do .pivot_table ( value index ,, -->aggfunc=np.sum<--) use like that




