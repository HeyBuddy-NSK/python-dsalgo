class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def _parent(self,index):
        """
        Calculates the index for parent node
        """
        return (index-1)//2
    
    def _left_child(self,index):
        """
        Calculates the index for left child node.
        """
        return 2*index+1
    
    def _right_child(self,index):
        """
        Calculates the index for right child node.
        """
        return 2*index+2
    
    def insert(self,data):
        """
        Inserts value given by user into the heap structure.
        """
        self.heap.append(data)
        index = len(self.heap)-1
        
        # Bubble Up
        while index>0:
            parent = self._parent(index)
            if self.heap[index]>self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
                
    def delete_node(self,data):
        """
        Deletes node with given value by user.
        """
        try:
            index = self.heap.index(data)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            
            # Bubble down
            if index < len(self.heap):
                
                while True:
                    left = self._left_child(index)
                    right = self._right_child(index)
                    largest = index
                    
                    if left<len(self.heap) and self.heap[left] > self.heap[largest]:
                        largest = left
                        
                    if right<len(self.heap) and self.heap[right]>self.heap[largest]:
                        largest = right
                    if largest!=index:
                        self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                        index = largest
                        
                    else:
                        break
                    
                # Bubble up
                while index > 0:
                    parent = self._parent(index)
                    if self.heap[index]>self.heap[parent]:
                        self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
                        index = parent
                        
                    else:
                        break
                        
        except ValueError:
            print(f"Value {data} not found in the heap")
            
    def get_max(self):
        """
        Returns maximum value from heap.
        """
        return self.heap[0] if self.heap else "Heap is Empty"
    
    def print_all(self):
        """
        Prints max heap.
        """
        print(self.heap)