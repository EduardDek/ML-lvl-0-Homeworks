
eps = 0.0000000001
n = int(input("n="))
for i in range(n,0,-1):
    
    if abs(round(i**(1/3),0) - (i**(1/3)))< eps:
        
        print(i)
        break 
