def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#fib(1) -> 2^1 steps
#fib(2) -> 2^2 steps
#fib(3) -> 2^3 steps
#total work: 2^1 + 2^2 ... 2^n
#2^(n+1) - 2 == O(2^n)