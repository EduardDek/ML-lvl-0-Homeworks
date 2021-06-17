a = int(input("a="))
print(a)

while a>=10:
    mysum = 0
    while a>=1:
    
        if(round((a/10-int(a/10))*10))!=0:
            mysum +=round((a/10-int(a/10))*10)
   
        a=int(a/10)

    print(mysum)
    a=1*mysum

    
