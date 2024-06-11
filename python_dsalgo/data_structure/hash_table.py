class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self,key):
        """Generate Hash Index for given value"""
        return hash(key) % self.size

    def insert(self,value):
        """Inserts Hash value in the table."""
        index = self._hash(value)

        if value not in self.table[index]:
            self.table[index].append(value)

    def search(self,value):
        """This function searches for the value in table."""
        index = self._hash(value)

        if value in self.table[index]:
            return f'Found the value {value} at index {index} .'
        else:
            return f"value {value} not found in the table."

    def delete(self,value):
        """This function deletes value from the function."""
        index = self._hash(value)
        if value in self.table[index]:
            self.table[index].remove(value)
            return f"Value {value} deleted from the table."

        else:
            return f"Value {value} not fount in the table."

    def print_table(self):
        """This function prints whole table contents."""
        for index, bucket in enumerate(self.table):
            print(f"{index} : {bucket}")