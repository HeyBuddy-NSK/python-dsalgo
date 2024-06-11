# For node creation
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# Linked list class

class CircularDoublyLinkedList:
    def __init__(self):
        """
        Circular Doubly linked list implementation
        """
        self.head = None
        
    def append(self, data):
        """
        This function Adds value at the end of list
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        
        last_node = self.head.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node
        
        return
    
    def delete_with_value(self,data):
        """
        This function deletes node using given value/Data.
        """
        if not self.head:
            return "list is empty"
        
        current_node = self.head
        while True:
            if current_node.data == data:
                if current_node.next == self.head and current_node.prev == self.head:
                    self.head = None
                    
                else:
                    if current_node == self.head:
                        self.head = current_node.next
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                        
                return "Node Deleted."
            
            current_node = current_node.next
            if current_node == self.head:
                break
                
    
    def print_list(self):
        """
        This function prints all values from the linked list.
        
        OR

        This function prints the circular doubly linked list.
        """
        if not self.head:
            return "List is empty."
        
        current_node = self.head
        while True:
            print(current_node.data, end = "<->")
            current_node = current_node.next
            if current_node==self.head:
                break
                
        print("Circular")