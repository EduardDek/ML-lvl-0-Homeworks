a12 = [float(input("a1=")),float(input("a2="))]
b12 = [float(input("b1=")),float(input("b2="))]

     

if min(a12)<=min(b12):
    minsect = a12
else:
    minsect = b12

if max(a12)>=max(b12):
    maxsect = a12
else:
    maxsect = b12

if maxsect!=minsect:
    print (max((max(minsect)-min(maxsect)),0))
else:
    print(min(abs(a12[0]-a12[1]),abs(b12[0]-b12[1])))
    




