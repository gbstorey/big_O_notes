def printUnorderedPairs (arrayA, arrayB):
    for i in range(len(arrayA)): #-----A
        for j in range(len(arrayB)): #--- B
            if arrayA[i] < arrayB[j]: #--- constant
                print(str(arrayA[i]) + "," + str(arrayB[j]))  #-- constant

#What is the runtime of this code?
# O(a*b)
