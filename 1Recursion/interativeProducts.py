#Recursive Exercise 1 Iterative Products Delivery

# interation
houses = ["A house", "B house", "C house", "D house"]
def deliverProductsInteratively():
    for house in houses:
        print(house)
    
deliverProductsInteratively()


#Recursive Exercise 2
# recursive
# first seperate from full house to be half until it have only one to print and recursive to print nad havling again
def deliverProductsRecursively(houses):
    # base case only 1
    if len(houses) == 1:
        house = houses[0]
        print(house)
    
    # recursive case more than 1
    else: 
        # separate mid
        mid = len(houses) // 2
        firstHalf = houses[:mid]  # first half of houses amount
        secondHalf = houses[mid:]  # second half of houses amount

        # divides his work among two work
        deliverProductsRecursively(firstHalf)
        deliverProductsRecursively(secondHalf)

deliverProductsRecursively(houses)