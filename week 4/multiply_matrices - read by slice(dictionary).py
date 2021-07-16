import time


def median_space(txt):
    spacecount = len(txt)-len(txt.replace(" ",""))+1
    if spacecount == 0:
        return len(txt)
    med_space = spacecount//2
    counter = 0
    final = -1
    for i in txt:
        final +=1
        if i == " ":
            counter+=1
            if counter == med_space:
                return final

def convert_dict (lst, startrange):
    mydict ={}
    for val in lst:
        mydict.update({startrange:val})
        startrange +=1
    return mydict                

def Save_Matrix(filename, matrixname):
    with open(filename, 'w') as f:
        for row in matrixname:
            f.write(' '.join(map(lambda x: str(x), row)))
            f.write('\n') 

def multiply_matrix(M1_Name,M2_Name,M2_Last_row):
    newmatrix = []
    curlist_M1 = []
    curlist_M2 = []
    curdict_M1={}
    curdict_M2={}
    
    M1_Finished = False
    M2_Finished = False
    second_chunk_M1 = ""
    second_chunk_M2 = ""
    M1_curr_row = 0
    M2_curr_row = 0
    change_row_M1 = False
    change_row_M2 = False
    val_counter_M1 = 0
    val_counter_M2 = 0

    
    with open (M1_Name, 'r') as f1:
        while M1_Finished == False:
            
            M1_curr_row +=1 if change_row_M1==True else 0
            val_counter_M1=0 if change_row_M1==True else val_counter_M1
            change_row_M1 = False
            chunk_M1 = f1.read(2000)
            M1_Finished = True if not chunk_M1 else False
               
            chunk_M1 = second_chunk_M1 + chunk_M1
            if "\n" in chunk_M1:
                first_chunk_M1 = chunk_M1[0:chunk_M1.find("\n")]
                second_chunk_M1 = chunk_M1[chunk_M1.find("\n")+1:len(chunk_M1)]
                change_row_M1 = True
                
            else:
                med = median_space(chunk_M1)
                first_chunk_M1 = chunk_M1[0:med]
                second_chunk_M1 = chunk_M1[med:len(chunk_M1)]

            
            
            curlist_M1 = list(map(int,first_chunk_M1.split()))
            curdict_M1 = convert_dict(curlist_M1,val_counter_M1)
            val_counter_M1 += len(curlist_M1)
            #print (curdict_M1, "row=", M1_curr_row, "Matrix M1")
            chunk_M1 = second_chunk_M1
            
        
            with open (M2_Name, 'r') as f2:
                    f2.seek(0,0)
                    M2_Finished = False
                    while M2_Finished == False:
                        M2_curr_row +=1 if change_row_M2==True else 0
                        M2_curr_row = 0 if M2_curr_row == M2_Last_row else M2_curr_row
                        val_counter_M2=0 if change_row_M2==True else val_counter_M2
                        change_row_M2 = False
                        chunk_M2 = f2.read(2000)
                        M2_Finished = True if not chunk_M2 else False
                           
                        chunk_M2 = second_chunk_M2 + chunk_M2
                        if "\n" in chunk_M2:
                            first_chunk_M2 = chunk_M2[0:chunk_M2.find("\n")]
                            second_chunk_M2 = chunk_M2[chunk_M2.find("\n")+1:len(chunk_M2)]
                            change_row_M2 = True
                            
                        else:
                            med = median_space(chunk_M2)
                            first_chunk_M2 = chunk_M2[0:med]
                            second_chunk_M2 = chunk_M2[med:len(chunk_M2)]

                        
                        
                        curlist_M2 = list(map(int,first_chunk_M2.split()))
                        curdict_M2 = convert_dict(curlist_M2,val_counter_M2)
                        val_counter_M2 += len(curlist_M2)
                        #print (curdict_M2, "row=", M2_curr_row, "Matrix M2")
                        chunk_M2 = second_chunk_M2

                        
                        for i in curdict_M1:
                            try:
                                curdict_M2[i]
                                try:
                                    newmatrix[M1_curr_row]
                                except:
                                    newmatrix.append([0])
                                try:
                                    newmatrix[M1_curr_row][M2_curr_row]
                                except:
                                    newmatrix[M1_curr_row].append(0)
                                newmatrix[M1_curr_row][M2_curr_row]+=  curdict_M1[i]* curdict_M2[i]
                            except: continue
                        
                                

    return (newmatrix)
                             
t = time.time()   
mmult = multiply_matrix("A.txt","B.txt",M2_Last_row)
Save_Matrix('mmult_long.txt', mmult)
print ((time.time()-t)/60,"minutes")









