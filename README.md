# Python Data Structures and Algorithms Package

This repository contains a Python package implementing various data structures and algorithms. It's designed as a beginner project to help understand and practice fundamental concepts of python package creation.

## Table of Contents

- [Python Data Structures and Algorithms Package](#python-data-structures-and-algorithms-package)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Modules](#modules)
    - [data\_structure](#data_structure)
    - [searching](#searching)
    - [sorting](#sorting)
  - [Contributing](#contributing)
  - [License](#license)

## About

The Python Data Structures and Algorithms package includes implementations of common data structures (like lists, stacks, queues, trees, and graphs) and algorithms (like searching and sorting). This package is an educational resource.

## Installation

First, clone the repository and navigate to the directory:

```bash
git clone https://github.com/HeyBuddy-NSK/python-dsalgo.git
cd python-dsalgo
```

Then, install the package:
```bash
pip install .
```

**OR**

Install directly using pip.

```bash
pip install python-dsalgo
```

## Usage

After installing the package, you can use it in your Python scripts. Here's an example of how to use the sorting module:

```python
from python_dsalgo.sorting import quick_sort

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
```

## Modules

### data_structure

- `singly_linked_list.py` : Implementation of singly linked list.
  - **Functions / Methods:**
    - `append(data)` : Appends data to the end of list.
    - `add_at_start(data)` : Adds data to the start of list.
    - `delete_with_value(Target_value)` : Delete node from list with given value by user
    - `print_list()` : Prints whole list.
    - `search(key_data)` : Performs search operation for given data in the list.
    - `get_length()` : returns length of list.
  
  - **Usage**
  
    ```python
    from python_dsalgo.data_structure import SinglyLinkedList

    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.print_list()
    ```


- `doubly_linked_list.py` : Implementation of doubly linked list.
  - **Functions / Methods:**
    - `append(data)` : Appends data to the end of list.
    - `add_at_start(data)` : Adds data to the start of list.
    - `delete_with_value(Target_value)` : Delete node from list with given value by user
    - `print_list()` : Prints whole list.
    - `search(key_data)` : Performs search operation for given data in the list.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import DoublyLinkedList

    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display()
    ```

- `circular_singly_linked_list.py` : Implementation of circular singly linked list.
  - **Functions / Methods:**
    - `append(data)` : Appends data to the end of list.
    - `add_at_start(data)` : Adds data to the start of list.
    - `delete_with_value(Target_value)` : Delete node from list with given value by user
    - `print_list()` : Prints whole list.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import CircularSinglyLinkedList

    csll = CircularSinglyLinkedList()
    csll.append(1)
    csll.append(2)
    csll.append(3)
    csll.print_list()
    ```


- `circular_doubly_linked_list.py` : Implementation of circular doubly linked list
  - **Functions / Methods:**
    - `append(data)` : Appends data to the end of list.
    - `delete_with_value(Target_value)` : Delete node from list with given value by user
    - `print_list()` : Prints whole list.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import CircularDoublyLinkedList

    cdll = CircularDoublyLinkedList()
    cdll.append(1)
    cdll.append(2)
    cdll.append(3)
    cdll.print_list()
    ```

- `stack.py`: Implementation of stacks.
  - **Functions / Methods :**
    - `push(data)` : Add / push data to the top of stack.
    - `pop()` : Pops / deletes data from the top of stack. 
    - `isEmpty()` : Returns True if stack empty else returns False.
    - `peek()` : Returns value at the top of stack.
    - `size()` : Get size of stack.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import Stack

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    ```

- `queue.py`: Implementation of queues.
  - **Functions / Methods :**
    - `enqueue(data)` : Inserts data into queue.
    - `dequeue()` : Deletes data from queue.
    - `front()` : Returns value from the front of queue.
    - `rear()` : Returns value from the rear of queue.
    - `isEmpty()` : Checks if queue is empty or not. Returns True if queue is empty else False.
    - `size()` : Returns size of queue.
  - **Usage**
    ```python
    from python_dsalgo.data_structure import Queue

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    ```

- `binary_search_tree.py`: Implementation of binary search tree.
  - **Functions / Methods :**
    - `insert(key)` : Insert a new node with the given key / data.
    - `search(key)` : Search for a node with the given key.
    - `delete(key)` : Delete a node with the given key.
    - `inorder()` : Perform an inorder traversal.
  
  - **Usage**
    ```python
    from Python_dsalgo.data_structure import BinarySearchTree

    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.inorder()
    ```

- `graph_AL.py`: Implementation of graph adjacency list representation.
  - **Functions / Methods :**
    - `add_edge(u,v)` : Addes edge in graph between two vertices u and v.
    - `print_graph()` : prints adjacency list representation of graph.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import GraphAL

    graph = GraphAL()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.print_graph()
    ```
 
- `graph_AM.py` : Implementation of graph adjacency matrix representation.
  - **Functions / Methods :**
    - `add_edge(u,v)` : Addes edge in graph between two vertices u and v.
    - `print_graph()` : Prints Adjacency Matrix representation of graph.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import GraphAM

    # While creating object you have to give how many virtices you will. e.g here it is 3.
    graph = GraphAM(3)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.print_graph()
    ```

- `hash_table.py` : Implementation of hash table.
  - **Functions / Methods :**
    - `insert(value)` : Inserts Hash value in the table.
    - `search(value)` : This function searches for the value in table.
    - `delete(value)` : This function deletes value from the function.
    - `print_table()` : This function prints whole table contents.
  
  - **Usage** 
    ```python
    from python_dsalgo.data_structure import HashTable

    ht = HashTable()
    ht.insert('value1')
    ht.insert('value2')
    print(ht.search('value2'))
    ht.print_table()
    ```

- `max_heap.py` : implementation of max heap.
  - **Functions / Methods :**
    - `insert(data)` : Inserts value given by user into the heap structure.
    - `delete_node(data)` : Deletes node with given value by user.
    - `get_max()` : Returns maximum value from heap.
    - `print_all()` : Prints max heap.
  
  - **Usage**
    ```python
    from python_dsalgo.data_structure import MaxHeap

    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(5)
    max_heap.insert(20)
    print(max_heap.get_max())
    max_heap.print_all()
    ```


- `min_heap.py` : implementation of min heap. 
  - **Functions / Methods :**
    - `insert(data)` : Inserts value given by user into the heap structure.
    - `delete_node(data)` : Deletes node with given value by user.
    - `get_min()` : Returns minimum value from heap.
    - `print_all()` : Prints min heap.

  - **Usage**
    ```python
    from python_dsalgo.data_structure import MinHeap

    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(20)
    print(min_heap.get_min())
    min_heap.print_all()
    ```
  

### searching

- `binary_search`: Implementation of searching algorithm binary search.
  - **Method**
    `binary_search(array,target)` : Returns index of element if found.

  - **Usage**
    ```python
    from python_dsalgo.searching import binary_search

    arr = [1, 2, 3, 4, 5]
    index = binary_search(arr, 3)
    print(index)
    ```

- `linear_search`: Implementation of searching algorithm linear search.
  - **Method**
    `linear_search(array,target)` : Returns index of element if found.

  - **Usage**
    ```python
    from python_dsalgo.searching import linear_search

    arr = [1, 2, 3, 4, 5]
    index = linear_search(arr, 3)
    print(index)
    ```
 

- `bfs` : Implementation of breadth first search algorithm.
  - **Method**
    `bfs(graph, starting_vertex)` : Returns order list in wich order graph was visited.

  - **Usage**
    ```python
    from python_dsalgo.searching import bfs

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    order_list = bfs(graph, 'A')
    print(order_list)
    ```

- `dfs` : Implementation of depth first search algorithm.
  - **Method**
    `dfs(graph, starting_vertex)` : Returns order list in wich order graph was visited.


  - **Usage**
    ```python
    from python_dsalgo.searching import dfs

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    order_list = dfs(graph, 'A')
    print(order_list)
    ```
 

### sorting

- `bubble_sort` : Implementation of sorting algorithm bubble sort.
  - **Method**
    `bubble_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import bubble_sort

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)
    ```

- `bucket_sort` : Implementation of sorting algorithm bucket sort.
  - **Method**
    `bucket_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import bucket_sort

    arr = [0.25, 0.36, 0.58, 0.41, 0.29, 0.22, 0.93, 0.44, 0.60, 0.75]
    sorted_arr = bucket_sort(arr)
    print(sorted_arr)
    ```

- `counting_sort` : Implementation of sorting algorithm counting sort.
  - **Method**
    `counting_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import counting_sort

    arr = [4, 2, 2, 8, 3, 3, 1]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)
    ```

- `heap_sort` : Implementation of sorting algorithm heap sort.
  - **Method**
    `heap_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import heap_sort

    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(arr)
    print(sorted_arr)
    ```

- `insertion_sort` : Implementation of sorting algorithm insertion sort.
  - **Method**
    `insertion_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import insertion_sort

    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
    ```

- `merge_sort` : Implementation of sorting algorithm merge sort.
  - **Method**
    `merge_sort(array)` : Returns sorted array.

  - **Usage** 
    ```python
    from python_dsalgo.sorting import merge_sort

    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    ```

- `quick_sort` : Implementation of sorting algorithm quick sort.
  - **Method**
    `quick_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from ptyhon_dsalgo.sorting import quick_sort

    arr = [10, 7, 8, 9, 1, 5]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
    ```

- `radix_sort` : Implementation of sorting algorithm radix sort.
  - **Method**
    `radix_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import radix_sort

    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)
    ```

- `selection_sort` : Implementation of sorting algorithm selection sort.
  - **Method**
    `selection_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import selection_sort

    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print(sorted_arr)
    ```

- `shell_sort` : Implementation of sorting algorithm shell sort.
  - **Method**
    `shell_sort(array)` : Returns sorted array.

  - **Usage**
    ```python
    from python_dsalgo.sorting import shell_sort

    arr = [12, 34, 54, 2, 3]
    sorted_arr = shell_sort(arr)
    print(sorted_arr)
    ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.