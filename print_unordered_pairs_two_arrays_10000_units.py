def printUnorderedPairs (arrayA, arrayB):
    for i in range(len(arrayA)): #-----A
        for j in range(len(arrayB)): #--- B
            for k in range(0, 10000): #---- still a constant
                print(str(arrayA[i]) + "," + str(arrayB[j]))  #-- constant

#Runtime of this code:
#O(a*b)