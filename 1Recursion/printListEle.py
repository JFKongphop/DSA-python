#Recursive Exercise 5.1 
# print all element in list by recursive
def attachHead(elelement, inputList):
    return [elelement] + inputList

result = attachHead('I',                                           # 4 return ["I", "Love", "Recursion", 555]
                    attachHead('Love',                             # 3 return ["Love", "Recursion", 555]
                                attachHead('Recursion',            # 2 return ["Recursion", 555]
                                            attachHead(555, [])))) # 1 return [555]
# ['I', 'Love', 'Recursion', 555] append it in the list | compile from inner list to outside

# counting the number of people before me and return my position
def howManyIn(peopleList):
    # check people in list is can count to the last
    if peopleList[1:]:
        print('Me and the guys behind')

        # increment of the number of my position
        return 1 + howManyIn(peopleList[1:])
    
    else:
        print('Just me')
        return 1
    
result1 = howManyIn([i for i in range(5)])


