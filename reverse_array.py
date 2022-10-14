def reverse(array):
    for i in range(0, int(len(array)/2)): #n/2
        other = len(array)-i-1 #assignment: constant
        temp = array[i] #assignment: constant
        array[i] = array[other] #assignment: constant
        array[other] = temp #assignment: constant
    print(array)

#runtime of this code:
#O(n)