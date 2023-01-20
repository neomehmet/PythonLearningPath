def summ(numb1, numb2):
    return  numb1+numb2

## try except & finally

while True:
    try :
        x = int(input("enter number : "))
        y = int(input("enter number : "))
    except : # if enter not a number algorythm come here
        print("please enter a number")
        continue
    else :
        print("thanks")
        break
    finally : #algorythm come here all conditions
        print(" in finally scope ")