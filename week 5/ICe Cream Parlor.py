t = int(input("how many times?"))


for i in range(0,t):
    found = False
    money = int(input("money="))
    CostSize = int(input("Cost size="))
    cost = []
    for j in range (0,CostSize):
        cost.append(int(input("Cost")))
    for e in range (0,len(cost)):
        for c in range(e+1,len(cost)):
            if cost[e]+cost[c]==money:
                print(e+1,c+1)
                found = True
                break
        if found == True:
            break
        
    
