import pandas as pd

dataFrame = pd.read_excel("fileNeme.xlsx")
dataFrameWithOutNULLVAL = dataFrame.dropna()
dataFrameWithOutNULLVAL.to_excel("newExcelFile.xlsx")

#read_csv
#to_csv

 