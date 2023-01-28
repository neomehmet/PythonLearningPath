# data frames is may think merged series

import numpy as np
import pandas as pd

dataMatrix = np.random.randn(4,3)   # n comes from normal disturbition
dataFrame = pd.DataFrame(dataMatrix)
print(dataFrame) # display like an excell table vohooo what amazing library

print(dataFrame[0]) # first colomn
dataFrame2 = pd.DataFrame(dataMatrix,index = ["fatih","osman","suleyman","murad"],columns=["salary","age","ruleYear"])

print(dataFrame2)
print(dataFrame2["age"])
print(dataFrame2["ruleYear"])
print(dataFrame2[["salary","age"]])  #dataFrame2 [ [ x,x ] ] colomn selection

#line selection...
selectFatih = dataFrame2.loc["fatih"]
print("\n\n")
print(selectFatih)
selectLineindex = dataFrame2.iloc[0]
print("\n",selectLineindex)