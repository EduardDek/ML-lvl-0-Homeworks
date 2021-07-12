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

def multiply_matrix(M1name,M2name):
    M1_Rows = 0
    M1_Cols = 0
    M2_Rows = 0
    M2_Cols = 0
    rows_m1 = 0
    rows_m2 = 0
    
    with open (M1name, 'r') as f:
        for line in f:
            M1_Rows +=1
        f.seek(0, 0)
        firstrow = f.readline()
        M1_Cols = len(firstrow)-len(firstrow.replace(' ',''))+1

    with open (M2name, 'r') as f2:
        for line in f2:
            M2_Rows +=1
        f2.seek(0, 0)
        firstrow = f2.readline()
        M2_Cols = len(firstrow)-len(firstrow.replace(' ',''))+1

    newmatrix = create_blank_matrix((M1_Rows,M2_Cols))
    
    with open (M1name, 'r') as f:
        with open (M2name, 'r') as f2:
            while rows_m1 < M1_Rows:
                current_row_m1 = list(map(int,f.readline().replace("\n","").split()))
                rows_m1+=1
                rows_m2 = 0
                f2.seek(0, 0)
                while rows_m2 < M2_Rows:
                    current_row_m2 = list(map(int,f2.readline().replace("\n","").split()))
                    rows_m2+=1
                    for a in range(0,M2_Cols):
                        newmatrix[rows_m1-1][a]+= current_row_m1[rows_m2-1]*current_row_m2[a]

    return newmatrix

def Save_Matrix(filename, matrixname):
    with open(filename, 'w') as f:
        for row in matrixname:
            f.write(' '.join(map(lambda x: str(x), row)))
            f.write('\n')


        
#if __name__ == '__main__':

t = time.time()
mmult = multiply_matrix('A.txt','B.txt')
#Save_Matrix('mmult.txt', mmult)
print ((time.time()-t)/60,"minutes")

#6.7 minutes including writing the file
#6.6 minutes without writing the file
