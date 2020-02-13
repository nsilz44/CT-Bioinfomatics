import numpy as np 


# recursion to lower the size of the matrix
def Q(matrixD):
    matrixQ = np.zeros((len(matrixD[:,0]),len(matrixD[:,0])))
    lowestQ = 0
    for j in range(0,len(matrixQ[0])):
        for i in range(0,len(matrixQ[0])):
            if i == j:
                matrixQ[j][i] = 0
            else:
                matrixQ[j][i] = (len(matrixD)-2) * matrixD[j][i] - matrixD[j][-1] - matrixD[i][-1]
                if matrixQ[j][i] < lowestQ:
                    k = j
                    l = i
    print (k,l)
    print(matrixQ)
    matrixN = np.zeros(((len(matrixQ[0])-1),len(matrixQ[0])-1))
    m = 0
    for j in range(0,len(matrixN[0])):
        n = 0
        print(matrixN)
        if m == k or m == l:
            m = m + 1
            if m == k or m == l:
                m = m + 1
        for i in range(0,len(matrixN[0])-1):
            if n == k or n == l:
                    n = n + 1
                    if n == k or n == l:
                        n = n + 1
            matrixN[j][i] = matrixD[m][n]
            n = n + 1
            print(i,j)
        matrixN[j][-1] = 0.5 * (matrixD[m][k] + matrixD[m][l] - matrixD[l][k])
        m = m + 1
            
    
file1 = open('matrix1.txt', 'r')
arrayD = file1.read()
arrayD = [item.split() for item in arrayD.split('\n')[:]]
file1.close()
d = np.zeros(((len(arrayD[0])-1),len(arrayD[0])))
j = 0
i = 0
for j in range(1,len(arrayD[0])):
    score = 0
    for i in range(1,len(arrayD[0])):
        m = float(arrayD[i][j])
        d[j-1][i-1] = m
        score = score + m
    d[j-1][-1] = score
print(d)
Q(d)


               
    

