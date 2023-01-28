# data frames is may think merged series

import numpy as np
import pandas as pd
dataMatrix = np.random. randn(4,3)
dataFrame2 = pd.DataFrame(dataMatrix,index = ["fatih","osman","suleyman","murad"],columns=["salary","age","ruleYear"])

# ad new colomn
print(dataFrame2)
dataFrame2["kids"] = dataFrame2["age"] + dataFrame2["age"]
print(dataFrame2)
# delete a colomn
dataFrame3 = dataFrame2.drop("kids",axis=1) # axis 1 is colomn
print(dataFrame3)
#delete line
dataFrame3 = dataFrame2.drop("fatih")
print(dataFrame3)

print("\n\n")

dataFrame2.drop("age", inplace = True,axis=1)
print(dataFrame2) # age coloms goes...
print(dataFrame2.loc["fatih","kids"] )           #or
print(dataFrame2.loc["fatih"]["kids"])

#bool op

print( dataFrame2 < 1)
boolFrame = dataFrame2 < 0
#or
boolFrame[dataFrame2 < 0]
print(boolFrame)
print("\n")
print(dataFrame2[boolFrame])
# upper line same as line below
print(dataFrame2[dataFrame2 < 0])

print(dataFrame2["kids"] < 1)
print(dataFrame2[dataFrame2["kids"] < 0])
# displaying lines that values smaller than zero on the kids colomn


v = np.array([ 0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

