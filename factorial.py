def factorial(n):  #---- M(n)
    if n < 0: #---constant
        return -1
    elif n == 0: #---constant
        return 1
    else: #------ M(n-1)
        return n * factorial(n-1)

#for factorial(3):
# M(n) = O(1) + M(n-1)
# M(0) = O(1)
# M(n-1)=O(1) + M((n-1)-1)
# M(n-2)=O(1) + M((n-2)-1)

# M(n) = 1(1+M((N-1)-1))
# = 2 + M(n-2)
# = 2 + 1 + M((n-2))-1)
# = 3 + M(n-3)
# M(n) = a + M(n-a)
# M(n) = n + M(n-n) = n

#O(n)