def  powersOf2(n):
    if n<1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2)) #logn
        curr = prev*2 #constant
        print(curr)
        return curr

#M(50):
#2*M(25)
#2*2*M(12)
#O(logn)


print(powersOf2(16))