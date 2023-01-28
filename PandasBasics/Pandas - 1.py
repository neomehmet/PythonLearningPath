import pandas as pd
import numpy as np
## series like nmpy array

Ages = {"John" : 50, "Julia": 40, "Bob":30 }
print(pd.Series(Ages))
Salary = {"Senior": 50000, "mid": 30000, "jr":10000}

mylist = [50,40,30]
print("\n",pd.Series(mylist))
print("\n",pd.Series(Ages))

myAges = [50,40,30]
myNames = ["John", "Julia","Bob"]
print(pd.Series(myAges))
print(pd.Series(myNames))
print(pd.Series(data=myAges, index=myNames) )
# series get first data, after index
# may think that a kind of excel tablo
npArr = np.array(myAges)
print(npArr)
print(pd.Series(npArr,myNames))

