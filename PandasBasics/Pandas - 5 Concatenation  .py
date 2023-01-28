import numpy as np
import pandas as pd
# concatenation
data = { "Name" :  ["ahmet","mehmet","zeynep","atıl"],
         "Spor" :  ["running","swimming","running","baseketbol"],
         "calori" : [ 200,100,50,300]
         }
data2 = { "Name" :  ["osman","levet","atlas","fatma"],
         "Spor" :  ["running","swimming","running","baseketbol"],
         "calori" : [ 200,100,50,300]
          }
data3 = { "Name" :  ["adam","bob","charles","david"],
         "Spor" :  ["running","swimming","golf","tennis"],
         "calori" : [ 200,100,250,500]
         }

Dframe1 = pd.DataFrame(data)
Dframe2 = pd.DataFrame(data2)
Dframe3 = pd.DataFrame(data3)
print(Dframe3)
print(Dframe1)
print(Dframe2)
df123 = pd.concat([Dframe1,Dframe2,Dframe3])
print(" concat below\n\n")
print(df123)
print("concat side\n\n")
dafr123 = pd.concat( [Dframe1, Dframe2, Dframe3],axis = 1)
print(dafr123)