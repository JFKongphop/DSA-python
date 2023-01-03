#Recursive Exercise 3
def factorialRecursive(n):
    # base case 1! = 1
    if n == 1:
        return 1
    
    # recursive case n! = n * (n-1)!
    # every time that decrement by 1 in the parameter then it equal 1
    else:
        return n * factorialRecursive(n - 1)
    
print(factorialRecursive(5))