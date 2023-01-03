# Recursive Excercise 6
def fibonacciRecursive(n):
    # base case
    if n <= 1:
        return n
    
    # recursive case
    else:
        return (fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2))
    
for i in range(100):
    print(fibonacciRecursive(i))