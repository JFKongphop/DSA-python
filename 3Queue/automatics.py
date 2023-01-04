#Queue Exercise 2 Creating Queue using list Built-in --> Automatics

queue = []

#Enqueue items to the Queue
for i in range(9):
    queue.append(i)
    print(queue)
    #print(f"{queue}".replace("[", "").replace("]", "").replace(", ", ""))

#print("".join([str(i) for i in range(10)]))
#Dequeue items from the Queue
while queue:
    print(queue)
    #print(f"{queue}".replace("[", "").replace("]", "").replace(", ", ""))
    queue.pop(0)
    