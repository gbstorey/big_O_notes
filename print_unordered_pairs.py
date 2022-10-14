# What is the runtime of the below code?

def printUnorderedPairs(array):
    for i in range(0, len(array)):  #-----------
        for j in range(i+1, len(array)):
            print(array[i] + "," + array[j])

#The range in the second loop goes by (n-1), (n-2)...
#Average work = n/2 * n
#1 + 2 + .... + (n-3) + (n-2) + (n-1)
#n(n-1)/2 = n^2 / 2 + n = n^2