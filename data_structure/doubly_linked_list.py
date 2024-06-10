# For creating node 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        """
        Doubly Linked List Implementation.
        """
        self.head = None
        
    def append(self,data):
        """
        This function adds the value at the end of list.
        """

        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        new_node.prev = last_node
        return
    
    def add_at_start(self,data):
        """
        This function adds the value at the start of list.
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        return
    
    def delete_by_value(self,data):
        """
        This function deletes the node using given value/data.
        """

        if not self.head:
            return "List is empty."
        
        if self.head.data == data:
            self.head = self.head.next
            return "Node deleted successfully."
        
        current_node = self.head
        
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                
                return "Node deleted successfully."
            current_node = current_node.next
            
        return "sorry node with given data not found."
    
    def print_list(self):
        """
        This function prints the list.
        """
        
        current_node = self.head
        while current_node:
            print(current_node.data,end="<->")
            current_node = current_node.next
            
        print("None")