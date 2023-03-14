class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0 
        

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1

        curr = self.head 
        for i in range(index):
            curr = curr.next
        return curr.val       

    def addAtHead(self, val: int) -> None:

        if self.head == None:
            new_node = Node(val)
            self.head = new_node
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            new_node = Node(val)
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            new_node = Node(val)
            temp.next = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            new = Node(val)
            new.next = curr.next
            curr.next = new
        self.size +=1


        

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.size:
            return
        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)