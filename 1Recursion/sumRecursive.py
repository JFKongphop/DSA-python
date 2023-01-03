#Recursive Exercise 4
def sumRecursive1(n):
    # base case 1! = 1
    if n == 1:
        return 1
    
    # recursive case n! = n * (n-1)!
    # every time that decrement by 1 in the parameter then it equal 1
    else:
        return n + sumRecursive1(n - 1)

sumRecursive1(5)

#Recursive Exercise 4.1
def sumRecursive2(currentNumber, accumulatedSum):
    # base case
    # return the final state
    if currentNumber == 11:
        return accumulatedSum
    
    # recursive case
    # thread the state through the recursive call
    else:
        return sumRecursive2(currentNumber + 1, accumulatedSum + currentNumber)

# first number with final result
sumRecursive2(1, 0)


#Recursive Exercise 4.2
# global mutable state
currentNumber = 1
accumulatedSum = 0
def sumRecursive3():
    global currentNumber
    global accumulatedSum

    # base case return final state when it done
    if currentNumber == 11:
        return accumulatedSum
    
    # recursive case
    # thread the state through the recursive call
    else:
        accumulatedSum += currentNumber # set the result sum and increment by 1
        currentNumber += 1 # increment by 1 with current number before sum in accumulatedSum in next round
        return sumRecursive3()

sumRecursive3()


#Recursive Exercise 4.3
# sum by recurivse in list
def listSumRecursive(numList):
    # base case
    if numList == []:
        return 0
    
    # recursive case
    else:
        head = numList[0]
        smallerList = numList[1:]
        return head + listSumRecursive(smallerList)

listSumRecursive([i for i in range(11)])