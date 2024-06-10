class MinHeap:
    def __init__(self):
        self.heap = []
        
    def _parent(self,index):
        """
        Calculates the index for parent node.
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
        Inserts the data/value given by the user into heap.
        """
        self.heap.append(data)
        index = len(self.heap)-1
        
        # Bubble up
        while index>0:
            parent = self._parent(index)
            if self.heap[index]<self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
                
            else:
                break
                
    def delete_node(self,data):
        """
        Deletes the node with given data/value by user.
        """
        try:
            index = self.heap.index(data)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            
            if index<len(self.heap):
                
                # Bubble down
                while True:
                    left = self._left_child(index)
                    right = self._right_child(index)
                    smallest = index
                    
                    if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
                        smallest = left
                    if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
                        smallest = right
                        
                    if smallest!=index:
                        self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                        index = smallest
                    else:
                        break
                        
                
                # Bubble Up
                while index>0:
                    parent = self._parent(index)
                    
                    if self.heap[index]<self.heap[parent]:
                        self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                        index = parent
                        
                    else:
                        break
        
        except ValueError:
            print(f"Value {data} not found in the heap.")
            
    
    def get_min(self):
        """
        Returns the minimum value from heap.
        """
        return self.heap[0] if self.heap else "Heap is empty."
    
    def print_all(self):
        """
        Prints the heap.
        """
        print(self.heap)