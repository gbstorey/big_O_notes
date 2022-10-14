#What is the runtime of the below code?

def foo(array):
    sum = 0 #----------------O(1)
    product = 1 #------------O(1)

    for i in array: #--------------O(len(array)) = O(n)
        sum += i #------------O(1)

    for i in array: #--------------O(len(array)) = O(n)
        product *= i #------------O(1)
    
    print ("Sum = "+str(sum)+", Product= "+str(product)) #------------O(1)

    # Total runtime: O(5+array+array) = O(5+2array) = O(array) = O(n)