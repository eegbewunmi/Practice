#creating a node object with methods
#create node class
class New_node:
   #Method for initializing node with a data and pointer
    def __init__ (self, data):
        self.data = data
        self.next = None
#Method to represent the printed or returned output of the New_node class
#Official representation of the object as a string
    def __repr__ (self):
        return "Node data = {}".format(self.data)
#Method for printing out the data in New_node
    def get_data (self):
        #print(self.data)
     return self.data

#Method for changing the data in the New_node
    def set_data (self, new_data):
        self.data = new_data

#Method for printing the node's pointer
    def get_next(self):
        return self.next

#Method for setting the node's pointer
    def set_next(self, node):
        self.next=node

#Create linkedlist class
class Linkedlist:
    def __init__ (self):
        self.head=None
#Check if the linked list is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
#Add a node to the front
    def add_front(self, data):
        temp = New_node(data)
        temp.next = self.head
        self.head = temp

#Return the size of the linkedlist
    def size(self):
        count= 0
        if self.head is None:
            return count

        current = self.head #Set it to the first node
        while current: #while the current node is not empty
            #current = current.get_next() #set the current node to the next node (for traversing the list)
            current =current.next
            count = count +1
        return "The size of the list is {}".format(count)

#Add to the end
    def append(self, data):
        temp =New_node(data)
    #get to the last part of the linkedlist
        current = self.head
        while current.next:
            current = current.next
        current.next = temp

#Get the data at a given position assuming head node is at position 1
    def get_position(self, position):
       index=1
       current=self.head
       while current:
           if index == position:
               return current
           current =current.next
           index += 1
       return "The position does not exist on the linked list"

#Insert data ( a node) to a sepcific index in the linked list
    def insert_node(self, data, position):
        i = 1
        current = self.head
        temp=New_node(data)
        if position == 1:
            temp.next = self.head
            self.head = temp
        while current:
            if (i == position - 1):
                    temp.next=current.next
                    current.next = temp
            current = current.next
            i=i+1
        #return "Invalid index"
#Delete the first Node
    def delete_first (self):
        self.head=self.head.next

#Delete the first instance of a node containing given get_data
    def delete_node (self, data):
        if (self.head.data==data):
            self.head=self.head.next
        else:
            current = self.head
            while current:
                if (current.next.data == data):
                    break
                    current=current.next
                current.next=current.next.next

#print out the data in the linkedlist
    def print_data (self):
        if self.head is None:
            return "The list is empty"
        else:
            list = []
            current=self.head
            while current:
                list.append(current.data)
                current=current.next
            return list

#Create a stack using a linked list
class Stack:
#create a linkedlist
    def __init__ (self):
        self.new_stack=Linkedlist()
#Add to stack (add to the front)
    def push(self, data):
        self.new_stack.add_front(data)

#Delete first item in Stack
    def pop(self):
        self.new_stack.delete_first()

#Print out all data in linked linkedlist
    def all_data(self):
        self.new_stack.print_data()

#testing
#Node1 = New_node('apple')
#Node2 = New_node('orange')

#Node1.get_data()
#print (Node1.get_data())
#Node2.set_data(50)
#print (Node2.get_data())
#Node1.set_next(Node2)
#print (Node1.get_next())
LL1=Linkedlist()
LL1.add_front('apple')
LL1.append('orange')
LL1.append(6)
LL1.insert_node('ebun', 2)
#print (LL1.is_empty())
#print (LL1.size())
#print (LL1.get_position(2))
#print (LL1.print_data())
LL1.delete_node('apple')
LL1.delete_node('ebun')
print (LL1.get_position(2))
print (LL1.print_data())

'''
stack1=Stack()
stack1.push(5)
stack1.push('ebun')
stack1.push('ebun')
stack1.push('ebun')
stack1.pop()
print (stack1.all_data())
'''
