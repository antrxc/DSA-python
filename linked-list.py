class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegining(self, data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if (self.head) is None:
            print("Empty List")
            return
        llstr=""
        itr = self.head
        while itr:
            llstr += str(itr.data) + "-->" 
            itr = itr.next
        
        print(llstr + "NULL")
    
    def insertAtEnd(self, data):
        node = Node(data,None)
        if self.head == None:
            self.insertAtBegining(data)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        
        

if __name__ == "__main__":
    ll=LinkedList()
    ll.insertAtBegining(5)
    ll.insertAtBegining(6)
    ll.insertAtBegining(7)
    ll.insertAtEnd(8)
    ll.print()