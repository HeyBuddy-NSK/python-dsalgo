class Queue:
    def __init__(self):
        self.queue_items = []
        
    def enqueue(self,data):
        """
        Inserts data into queue.
        """
        self.queue_items.append(data)
        return f"Data Added successfully."
    
    def dequeue(self):
        """
        Deletes data from queue.
        """
        if self.isEmpty():
            return "Queue is empty"
        
        return f"Data deleted {self.queue_items.pop(0)}"
    
    def front(self):
        """
        Returns value from the front of queue.
        """
        if self.isEmpty():
            return "Queue is empty"
        return f"Value at front : {self.queue_items[0]}"
    
    def rear(self):
        """
        Returns value from the rear of queue.
        """
        if self.isEmpty():
            return "Queue is empty"
        return f"Value at Rear : {self.queue_items[-1]}"
    
    def isEmpty(self):
        """
        Checks if queue is empty or not.
        """
        return len(self.queue_items)==0
    
    def size(self):
        """
        Returns size of queue.
        """
        if self.isEmpty():
            return "Queue is empty."
        return f"Size of queue is : {len(self.queue_items)}"
    
