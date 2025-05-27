Linked List Implementation in Python
This repository contains a basic implementation of a singly linked list in Python. It provides functionality to perform standard operations such as appending, prepending, inserting at a specific index, deleting elements, popping elements, and displaying the list.

Features
Create a linked list

Append elements to the end

Prepend elements to the beginning

Insert elements at a specific index

Delete an element by value

Pop an element by index or the last element if no index is provided

Display the list

Get the length of the list

Check if a value exists in the list

Class Descriptions
Node
Represents a single node in the linked list.

Attributes:
val: Stores the value of the node

next: Points to the next node in the list

Linked_List
Handles linked list operations.

Methods:
append(val): Adds a new node with val at the end

prepend(data): Adds a new node with data at the beginning

insert_index(index, data): Inserts a new node with data at the specified index

delete(data): Removes the first occurrence of data from the list

pop_s(index=None): Removes the element at index, or the last element if index is None

display(): Prints all values in the list

__len__(): Returns the length of the list

__contanis__(valu): Returns True if valu is in the list (note: method name is misspelled)

Example Usage
python
Copy
Edit
l1 = Linked_List()
l1.append(4)
l1.insert_index(0, 3)
l1.insert_index(0, 5)
l1.insert_index(1, 7)
l1.append(6)
l1.pop_s(1)
l1.display()
Output
Copy
Edit
5
7
3
4
6
Notes
Method __contanis__ appears to be a typo and should likely be renamed to __contains__ to work with Python's in keyword.

No exception handling is present; consider adding checks for edge cases (e.g. deleting or inserting from/to an empty list).

License
This project is open-source and available under the MIT License.
