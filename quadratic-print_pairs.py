# What is the runtime of the below code?

def printPairs(array):
    for i in array: #---------O(array*array)
        for j in array: #---------O(array)
            print(str(i) + ","+str(j)) #----------O(1)

#Total runtime: O(1+array + array*array) = O(array*array) = O(n^2)