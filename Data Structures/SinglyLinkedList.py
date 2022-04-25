class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def nextValue(self):
        if self.next == None:
            return "No Value"
        else:
            return self.next.value

class SLinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in the linked list
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def traverseList(self):
        if self.head is None:
            print("The singly Linked List doest not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    #Student implement searchSLL

    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None

# singlyLinkedList = SLinkedList()
# node1 = Node(1)
# node2 = Node(2)
#
# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2
#
# print(node.value for node in singlyLinkedList)

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(10,0)
singlyLinkedList.insertSLL(88,3)
singlyLinkedList.insertSLL(12,0)
print([node.value for node in singlyLinkedList])
# for node in singlyLinkedList:
#     print("Node value",node.value)
#     print("Node next", node.nextValue())
# singlyLinkedList.traverseList()
singlyLinkedList.deleteNode(4)
print([node.value for node in singlyLinkedList])