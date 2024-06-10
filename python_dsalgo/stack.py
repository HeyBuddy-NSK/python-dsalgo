class Stack:
    def __init__(self):
        self.stack_items = []
        
    def push(self,data):
        """
        Adds data in the stack.
        """
        self.stack_items.append(data)
        return "Data Added to stack."
    
    def pop(self):
        """
        Deletes data from the stack.
        """
        if self.isEmpty():
            return "Stack is empty."
        
        return f"Deleted {self.stack_items.pop()} from stack"
    
    def isEmpty(self):
        """
        Checks if the stack is empty or not.
        """
        return len(self.stack_items) == 0
    
    def peek(self):
        """
        returns value at the top of stack.
        """
        return self.stack_items[-1]
    
    def size(self):
        """
        returns size of stack.
        """
        return f"Size of stack is : {len(self.stack_items)}"