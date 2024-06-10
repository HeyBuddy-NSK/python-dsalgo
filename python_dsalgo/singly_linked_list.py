# for creating nodes with data and link to next node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# singly linked list class
class SinglyLinkedList:
    def __init__(self):
        """
        Singly linked list implementation.
        """
        self.head = None
    
    # for adding data at the end of list
    def append(self,data):
        """
        Adds value/data at the end of list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        return
    
    # for adding data/node at the start of the list
    def add_at_start(self,data):
        """
        Adds data/value at the start of list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # for deleting the node by value.
    def delete_with_value(self,data):
        """
        Deletes node from list by given value/data.
        """
        msg = None
        if not self.head:
            return "list is empty."
        
        if self.head.data == data:
            self.head = self.head.next
            return f"Node With value {data} deleted successfully."
        
        current_node = self.head
        prev_node = None
        while current_node.next:
            if current_node.data == data:
                msg = f"Node with value {data} Deleted successfully"
                break
            prev_node = current_node
            current_node = current_node.next
            
        if current_node is None:
            return "Data not found in list."
        
        prev_node.next = current_node.next
        
        # clearing temporary 
        current_node = None
        
        return msg
    
    # for printing list.
    def print_list(self):
        """
        Prints complete list with value if any.
        """
        current_node = self.head
        while current_node:
            print(f"{current_node.data}",end="->")
            current_node = current_node.next
        
        print("None")
        
    def search(self,data):
        """
        Searches for data in the list.
        """
        if self.head and self.head.data == data:
            return "Your data is in the head!."
        count = 0
        current_node = self.head
        while current_node:
            count = count+1
            if current_node.data == data:
                return f"Your data is in the {count} node."
            current_node = current_node.next
            
        return f"Your data is not in the List."
    
    def get_length(self):
        """
        Returns the length of the list.
        """
        if self.head and self.head.next == None:
            return 1
        
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
            
        return length