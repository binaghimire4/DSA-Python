#Recursion is the process of function calls itself within its own definition often breakdown a problem into smaller.

def fact(n):
    if n==0 or n ==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(10))

def fact(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        memo[n]=n
    else:
        memo[n] = fact(n-1, memo) + fact(n-2, memo)
    return memo[n]
print(fact(10))

