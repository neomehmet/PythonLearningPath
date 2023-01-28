import numpy as np
import pandas as pd

# missing values
data = {"istanbul":[30,29,np.nan],
        "kocaeli": [28,np.nan,30],
        "ankara":  [26,27,26]}

havaDurumu = pd.DataFrame(data)
print(havaDurumu)
print(havaDurumu.dropna()) #print(havaDurumu.dropna(axis=0))
print(havaDurumu.dropna(axis=1)) # 1 colomns, 0 lines
newData = {"istanbul":[30,29,np.nan],
        "kocaeli": [28,np.nan,30],
        "ankara":  [26,27,26],
        "sakarya": [23,np.nan,np.nan]}
newHavaDurumu = pd.DataFrame(newData)
print(newHavaDurumu)
print( newHavaDurumu.dropna(axis=1, thresh=2) ) # show till 2 nan values, others shall not pass :)

# set all value
print( newHavaDurumu.fillna(25))
print(newHavaDurumu)




