import numpy as np 
import numbers

def converter(element):
    try:
        return float(element)
    except ValueError:
        return element
file1 = open('matrix1.txt', 'r')
arrayD = file1.read()
arrayD = [item.split() for item in arrayD.split('\n')[:]]
file1.close()
matrixD = arrayD
for row in matrixD:
    score = 0
    for element in row:
        elements = converter(element)
        element = elements
        if type(elements)== float:
            score = score + element
    if score == 0:
        row.append('-')
    else:
        row.append(score)
print(matrixD)
