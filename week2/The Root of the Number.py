
a = int(input("a="))

mmult = 1
while a>=1:
    
    if(round((a/10-int(a/10))*10))!=0:
        mmult *=round((a/10-int(a/10))*10)
   
    a=int(a/10)

print (mmult)
