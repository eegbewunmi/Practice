#Create a queue using a list
class Queue:
    def __init__ (self):
        self.list = []
#Print out the first item on list
    def peek (self):
        return self.list[0]
#Remove the first item on list
    def dequeue (self):
        self.list.pop(0)

#Add to the list
    def enqueue(self, data):
        self.list.append(data)

#testing queue
Q1=Queue()
Q1.enqueue(45)
Q1.enqueue('ebun')
Q1.enqueue('bff')
Q1.dequeue()
print (Q1.peek())
