

def power(txt,power):
    newtext=""
    if power>0:
        for _ in range (0,power):
            newtext += txt
    print(newtext)

    if power<0:
        found = False
        ln = len(txt)
        for i in range (1, ln):
            counter = 1
            next_occ = txt[i:ln].find(txt[0])+i
            try:
                if ln//next_occ == ln/next_occ:
                    for k in range(1,ln//next_occ):
                        if txt[0:next_occ]==txt[k*next_occ:k*next_occ+next_occ]:
                            counter+=1

            except:
                continue
             
                
            if counter == int(ln//next_occ):
                
                found = True
                break

        if abs(power)>counter:
            print("undefined")

        else:
            print(txt[0:ln-(abs(power)*next_occ)+next_occ])


        
power("ab",1)
power("abc",0)
power("abcd",3)
power("xyzxyz",-2)
power("xyzxyz",-3)
power("xyzxyz",-1)
    
power("adadad",-1)
power("adadad",-2)
power("adadad",-3)
power("adadad",-4)

