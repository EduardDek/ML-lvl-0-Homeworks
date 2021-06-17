import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

try:
    largestangle = math.acos((a**2+b**2+c**2-2*max(a,b,c)**2)/(2*a*b*c/max(a,b,c)))/math.pi*180
    if largestangle == 180: print ("Not triangle") 
    if 90<largestangle < 180:print ("Obtuse triangle") 
    if largestangle == 90: print ("Right triangle") 
    if 0<largestangle < 90: print ("Acute triangle") 
except ValueError:
    print("NoT Triangle")




    




