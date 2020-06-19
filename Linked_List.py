# Linked List Implementation in Python By Ashutosh Deshpande
# All the comments are written for future understanding.

# Singly Linked List

# This implementation requires 2 classes

# 1. Node class

class Node:                     # This Class will specify the properties of the node
    def __init__(self,data):    # Initialize
        self.data = data        # Data is the data container of the node in linked list and Data is initailized here for the node
        self.next = None        # Next is the next part of the node that contains the address of the next node

# 2. Linked List class

class Linked_List:              # This Class specifies the properties of the linked list and contains all the operations of the linked list
    def __init__(self):         # Initialization
        self.head = None        # The head of the linked list is initialized here

# Inserting Elements in a Singly Linked List
# Types:
# 1. At the end of the list ; 
    
    def append(self,data):       # Append Class does the work of appending the new node at the end of the linked list
        new_node = Node(data)    # New Node is created here and initialized with the data

        if self.head is None:    # Check whether the list is empty and if empty
            self.head = new_node # then head will be the new node
            return               # return the list   
        
        last_node = self.head    # As we are appending the node to the last so the new node will be the last node and head is pointed to that node

        while last_node.next:    # Traverse the list until we reach the last node and when the next node is none then the loop will break
            last_node = last_node.next  # When we reach the last node then last node's next pointer should be pointing to the new last node
        last_node.next = new_node   # Last node's next pointer is now pointing to the new node


# 2. At the start of the list ; 

    def prepend(self, data):    # Prepend class does the work of insertig a node at the start of the list
        new_node = Node(data)   # Initialize the new node
        new_node.next = self.head # Assigning head to the next pointer of the new node
        self.head = new_node    # new node is the first node so head is now pointing to the new node

# 3. Somewhere in between the list

    def insert_after_node(self, prev_node, data):   # This function does the work of after a specified node that is passed as a parameter to this function
        
        new_node = Node(data)   # Initialize new node
        curr_node = self.head   # Current node is set here as the head node
        
        while(curr_node.data != prev_node): # This loop finds whether the current node's data is same as the passed node data string and traverses the list until the same is found
            curr_node = curr_node.next      # Until the passed node is not equal to the current node while traversing the list this will assign the next pointer to the next node to move forward
            if curr_node is None:           # if current node is none at this stage then diretly it prints out that node is not in the list and breaks out of the function 
                print("Previous node is not in the list")
                return
                                            # Here that node is now found i.e current node is now equal to the passed node
        new_node.next = curr_node.next      # we assign the new node's next pointer to the current node's next pointer so to attach that node to the new node
        curr_node.next = new_node           # and the current node's next pointer is the new node so in this way we establish the connection




# Print the linked list
    def print_list(self):
        current_node = self.head            # Head is pointing to the first node here
        while current_node:                 # Loop until current node is none
            print(current_node.data)        # Print the data of the current node
            current_node = current_node.next    # Current node's next is pointing to the next in line node


# Create an object of the Linked List class to use it further onwards
linkedlist = Linked_List()

# Append Class usage
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("D")

# Prepend class usage
linkedlist.prepend("E")

# Insert after a node usage
linkedlist.insert_after_node("B", "F")

# Print the list
linkedlist.print_list() 


