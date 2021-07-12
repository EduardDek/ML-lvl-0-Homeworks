import time

def read_matrix_from_file(filename):
    matrix = []
    with open (filename, 'r') as f:
        for line in f:
            matrix.append(list(map(int,line.replace("\n","").split())))
    return matrix

def create_blank_matrix(shape):
    matrix = []

    for i in range(0,shape[0]):
        matrix.append([])
        for _ in range(0,shape[1]):
            matrix[i].append(0)
    return matrix

def multiply_matrix(M1,M2):
    M1_Rows = len(M1)
    M1_Cols = len(M1[0])
    M2_Rows = len(M2)
    M2_Cols = len(M2[0])
    newmatrix = create_blank_matrix((M1_Rows,M2_Cols))

    for rows in range(0,M1_Rows):
        rowcounter = -1
        
       
        for cols in range(0,M2_Cols):
            colcounter = -1
            rowcounter+=1
            
            
            for val in M1[rows]:
                colcounter+=1
                newmatrix[rows][cols]+=val*M2[colcounter][rowcounter]
    return newmatrix
                
def Save_Matrix(filename, matrixname):
    with open(filename, 'w') as f:
        for row in matrixname:
            f.write(' '.join(map(lambda x: str(x), row)))
            f.write('\n')    
        

        
if __name__ == '__main__':
    A_matrix = read_matrix_from_file('A.txt')
    B_matrix = read_matrix_from_file('B.txt')
    #C_matrix = multiply_matrices(A_matrix, B_matrix)
    #write_matrix_to_file(C_matrix, 'result.txt')

#print(A_matrix)
#print(B_matrix)


t = time.time()
mmult = multiply_matrix(A_matrix,B_matrix)
#print (round(time.time()-t,4),"Seconds")
print ((time.time()-t)/60,"minutes")
Save_Matrix('mmult_long.txt', mmult)
#print (round(time.time()-t,4),"Seconds")
print ((time.time()-t)/60,"minutes")
#3.4 minutes :)


