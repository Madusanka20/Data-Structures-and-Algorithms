#Linked List Using Python

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class Sll:  # Initialize singly linked list
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node :
            yield node
            node =node.next

    def print(self):
        if self.head is None:
            print("No any Value")
        else:
            node=self.head
            while node is not None:
                print(node.value , end=" ")
                node=node.next
            print()    
    
    def insert(self, value, location): # insert a new node to anyplace 
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==-1:
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode 

    def search(self, serachValue): # Search any value from linkedList
        if self.head is None:
            print("No any Value")

        else:
            node=self.head
            while node is not None:
                if node.value ==serachValue:
                    print("Value found")
                    return
                node=node.next
            print("Value is not Found")    

    def delete(self , location):
        #remove first element
        if location==0: 
            if self.head.next==self.tail.head:# If only One element exist 
                self.head=None
                self.tail=None
            else :
                self.head=self.head.next

        elif location==-1:   
            if self.head.next==self.tail.head:# If only One element exist 
                self.head=None
                self.tail=None
            else:
                node=self.head
                while node is not None:
                    if node.next==self.tail:
                        break
                    node=node.next
                node.next=None
                self.tail=node   

        else:
            tempNode=self.head
            index=0
            while index<location-1:
                tempNode=tempNode.next
                index+=1

            nextNode=tempNode.next      
            tempNode.next=nextNode.next      




linkedList=Sll()
node1=Node(3)
node2=Node(5)

linkedList.head=node1
node1.next=node2
linkedList.tail=node2

linkedList.insert(8,1)
linkedList.insert(2,0)
linkedList.search(8)
linkedList.search(4)
linkedList.delete(2)
linkedList.print()  # output is 2 3 5 

