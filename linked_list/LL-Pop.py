class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

 
    def pop(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            temp = self.head
            pre = self.head

            while temp is not None:
                temp = temp.next
                if temp != None:
                    pre = pre.next
            self.tail = pre

            self.length -= 1

 


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop(2).value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop(1).value)
# (0) Items - Returns None
print(my_linked_list.pop(0))


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""