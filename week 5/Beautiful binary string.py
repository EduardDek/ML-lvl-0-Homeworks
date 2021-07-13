
def check_Beauty(binstring,moves=0):
    #print(moves,"fisrt line")
    if "010" in binstring:
        index = binstring.find("010")
        if index ==len(binstring)-3:
            binstring = binstring.replace("010","110",1)
        elif binstring[index+3] == 0:
            binstring = binstring.replace("010","110",1)
        else:
            binstring = binstring.replace("010","011",1)
        moves +=1
        check_Beauty(binstring,moves)

    #print(moves,"-last line")

    else:
        print(moves)
        #return moves

check_Beauty("01100")
check_Beauty("0100101010")
#print(check_Beauty("0100101010"))
