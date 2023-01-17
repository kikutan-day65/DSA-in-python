class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # createing a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # createing a new node
        # add node to end
        pass

    def prepend(self, value):
        # createing a new node
        # add node to fornt
        pass

    def insert(self, index, value):
        # createing a new node
        # insert node to the given index
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
