area = 12
panels = list()
i = area 
x = 0
while area > 0 :
    if i*i == area :
        panels.append(i*i)
        area = 0 
        print( " i = ",i," area = ",area )
        x = input("Press Enter to continue...")
        break
    elif i*i < area  :
        panels.append(i*i)
        area = area - i*i
        print( " i = ",i," area = ",area )
        x = input("Press Enter to continue...")  
    i = i - 1
    if i < 1:
        i = 1

print(panels)
print(panels)