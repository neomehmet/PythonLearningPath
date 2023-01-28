import numpy as np
import pandas as pd

vals = [101,202,303,404]
ages = [40,30,45,81]
names = ["bob","john","rambo","sly"]
xrandom = np.random.rand(4)
mDFrame = pd.DataFrame(data=vals, index=names, columns= ["Sample"])
mDFrame["Age"] = ages
mDFrame["NewColomnAdd"] = xrandom
print(mDFrame)
# how to change index
#mDFrame.reset_index(inplace=True)
#print(mDFrame)
print( mDFrame.reset_index() )
newindex = ["aaa","bbb","ccc","ddd"]
mDFrame["NewIndex"] = newindex
print(mDFrame)
mDFrame.set_index("NewIndex",inplace=True)
print(mDFrame)
print(mDFrame.loc["ccc"]) # just returns ccc line
print(mDFrame["Age"]) # just returns Age colomn


