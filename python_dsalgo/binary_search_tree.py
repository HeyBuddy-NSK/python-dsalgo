class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new node with the given key."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        """Helper method to insert a new node with the given key."""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def search(self, key):
        """Search for a node with the given key."""
        return self._search(self.root, key)

    def _search(self, current_node, key):
        """Helper method to search for a node with the given key."""
        if current_node is None or current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._search(current_node.left, key)
        else:
            return self._search(current_node.right, key)

    def delete(self, key):
        """Delete a node with the given key."""
        self.root = self._delete(self.root, key)

    def _delete(self, current_node, key):
        """Helper method to delete a node with the given key."""
        if current_node is None:
            return current_node
        
        if key < current_node.key:
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node.key:
            current_node.right = self._delete(current_node.right, key)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node with two children: Get the inorder successor
            current_node.key = self._min_value_node(current_node.right).key
            current_node.right = self._delete(current_node.right, current_node.key)
        
        return current_node

    def _min_value_node(self, node):
        """Helper method to find the node with the minimum key value."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Perform an inorder traversal."""
        self._inorder(self.root)

    def _inorder(self, node):
        """Helper method for inorder traversal."""
        if node is not None:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)