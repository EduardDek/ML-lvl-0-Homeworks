import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a!=0:
    eqtype = "Quadratic Equasation"
    D = b*b-4*a*c
    print(eqtype)
    print("Discriminant:",D)
    if D<0:
        print("No Solution")
    else:
        print("two solutions", (-b+math.sqrt(D))/2*a,(-b-math.sqrt(D))/2*a)

else:
    eqtype = "Non-quadratic equation"
    print(eqtype)
    if b==c==0:
        print ("Infinite Solutions")
    elif b==0:
        print ("No Solution")
    elif c==0:
        print ("One Solution", 0)
    else:
        print ("One Solution", -c/b)



    




