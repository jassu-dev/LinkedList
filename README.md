# Linked List Implementation in Python

This is a simple implementation of a singly linked list in Python. It includes basic operations like append, prepend, insert, delete, pop, and display.

## Features

- Append elements to the end of the list
- Prepend elements to the start of the list
- Insert elements at a specific index
- Delete an element by value
- Pop an element by index or the last element
- Display all elements in the list
- Get the length of the list
- Check if a value exists in the list

## Classes and Methods

### `Node`

Represents a single node in the list.

- `val`: The value stored in the node
- `next`: Pointer to the next node

### `Linked_List`

Manages the linked list and provides various methods:

- `append(val)`: Add a node with the specified value at the end
- `prepend(data)`: Add a node with the specified value at the beginning
- `insert_index(index, data)`: Insert a node at a given index
- `delete(data)`: Remove the first node with the given value
- `pop_s(index=None)`: Remove a node at the specified index, or the last node if no index is given
- `display()`: Print all elements in the list
- `__len__()`: Return the number of nodes in the list
- `__contanis__(valu)`: Check if a value exists in the list (note: typo in method name)

## Example Usage

```python
l1 = Linked_List()
l1.append(4)
l1.insert_index(0, 3)
l1.insert_index(0, 5)
l1.insert_index(1, 7)
l1.append(6)
l1.pop_s(1)
l1.display()
```

#Output
5
7
3
4
6

#Notes
The method __contanis__ is misspelled. To enable Python's in keyword, rename it to __contains__.

Basic error handling (e.g., out-of-range index) is not implemented and should be added for robustness.

#License
This project is licensed under the MIT License.
