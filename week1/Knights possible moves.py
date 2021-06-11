py= int(input ("input py"))
px= int(input ("input px"))

legalmovespy=[-1,1,2,-2]
legalmovespx=[-1,1,2,-2]

for  y in legalmovespy:
     for  x in legalmovespx:
        if abs(x)+abs(y)==3:
            if 0<py+y<9 and 0<px+x<9:
                print(py+y,px+x)





