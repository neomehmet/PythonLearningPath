#pandas series manupilation
import pandas as pd

pdSeriEx = pd.Series(["Alexander","Caesar","Mehmet2","Genghis","Timur","Attila"],[1,2,6,4,5,3] )
#print(pdSeriEx)

league = pd.Series([22,19,14],["Galata","fener","bjk"]) #historical series :)
cup = pd.Series([34,20,10], ["Galata","fener","bjk"] )
print(league)
print(cup)
print("galatasaray champ of league :",league["Galata"]   )
total = league + cup
print(total)


ser1 = pd.Series([1,2,3,4],["a","b","c","d"])
ser2 = pd.Series([10,20,30,40],["a","q","c","d"])
ser3 = ser1 + ser2
print(ser3)  # different index wont sum, they get NAN value
