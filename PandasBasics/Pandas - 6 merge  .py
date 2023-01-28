import numpy as np
import pandas as pd
# merging
dataM1 = { "Name" :  ["ahmet","mehmet","zeynep","atil"],
         "Spor" :  ["running","swimming","running","baseketbol"],
         }
dataM2 = { "Name" :  ["ahmet","mehmet","zeynep","atil"],
           "calori" : [ 200,100,50,300]
         }

dFm1 = pd.DataFrame(dataM1)
dFm2 = pd.DataFrame(dataM2)
print(dFm2)
print(dFm1)

mergedDF = pd.merge(dFm1,dFm2, on="Name") # common colomn must write "on"
print(mergedDF)