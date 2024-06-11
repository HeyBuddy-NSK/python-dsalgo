# for creating nodes with data and link to next node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        """
        Circular Linked List implementation.
        """
        self.head = None
        
    def append(self, data):
        """
        This function adds the value at the end of list.
        """
        new_node = Node(data) 
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        
        last_node = self.head
        while True:
            last_node = last_node.next
            if last_node.next == self.head:
                break
        
        last_node.next = new_node
        new_node.next = self.head
        
        return
    
    def add_at_start(self,data):
        """
        This function adds the value at the start of list.
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            return
        # for last node 
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next

        last_node.next = new_node
        new_node.next = self.head
        self.head = new_node
        
        return
    
    def delete_with_value(self,data):
        """
        This function deletes the node using given value/data.
        """

        if not self.head:
            return 'List is empty.'
        
        if self.head.data==data and self.head.next == self.head:
            self.head = None
            return "Last node deleted."
        
        current_node = self.head
        prev = None
        
        while True:
            if current_node.data == data:
                if prev:
                    prev.next = current_node.next
                else:
                    while current_node.next!= self.head:
                        current_node = current_node.next
                        
                    current_node.next = self.head.next
                    self.head = self.head.next
                return f"Node with value {data} deleted successfully."
            
            prev, current_node = current_node, current_node.next
            
            if current_node == self.head:
                break
                
        return "Data not found in the list."
        
    
    def print_list(self):
        """
        This function prints the list.
        """
        if not self.head:
            return "List is empty"
        
        temp = self.head
        while True:
            print(temp.data,end="->")
            temp = temp.next
            if temp == self.head:
                break
            